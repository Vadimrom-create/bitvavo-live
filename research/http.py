"""Public-only transport, bounded retries, shared rate limiting and replay log."""
from __future__ import annotations

import copy
import json
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

from research.common import utc


class PublicClient:
    def __init__(self, timeout=12, retries=3, requests_per_second=12):
        self.timeout, self.retries = timeout, retries
        self.spacing = 1 / requests_per_second
        self.lock = threading.Lock()
        self.next_request = 0.0
        self.pause_until = 0.0
        self.records = []
        self.cache = {}
        self.errors = []
        self.server_offset = 0.0
        # Additive transport telemetry only: these counters never alter pacing,
        # retry, caching or error semantics.
        self.metrics = {
            'request_attempts': 0,
            'successful_responses': 0,
            'pace_wait_seconds': 0.0,
            'rate_limit_wait_seconds': 0.0,
            'retry_backoff_seconds': 0.0,
            'rate_limit_resets_seen': 0,
        }

    @staticmethod
    def key(path, params):
        return path + '?' + urllib.parse.urlencode(sorted((params or {}).items()))

    def pace(self):
        with self.lock:
            now = time.monotonic()
            normal_schedule = max(now, self.next_request)
            scheduled = max(normal_schedule, self.pause_until)
            self.next_request = scheduled + self.spacing
            delay = max(0.0, scheduled - now)
            rate_limit_delay = max(0.0, scheduled - normal_schedule)
            self.metrics['pace_wait_seconds'] += delay
            self.metrics['rate_limit_wait_seconds'] += rate_limit_delay
        if delay > 0:
            time.sleep(delay)

    def get(self, path, params=None, retries=None, cache=True):
        if not (path in {'/time', '/markets', '/ticker/24h', '/ticker/book', '/ticker/price'}
                or re.fullmatch(r'/[A-Z0-9]+-EUR/(candles|book|trades)', path)):
            raise ValueError('public_endpoint_not_allowed')
        key = self.key(path, params)
        with self.lock:
            cached = self.cache.get(key) if cache else None
        if cached is not None:
            return copy.deepcopy(cached['data'])
        for attempt in range(retries or self.retries):
            self.pace()
            with self.lock:
                self.metrics['request_attempts'] += 1
            started = time.time()
            try:
                req = urllib.request.Request('https://api.bitvavo.com/v2' + key,
                    headers={'Accept': 'application/json', 'User-Agent': 'bitvavo-observatory/5.0'})
                with urllib.request.urlopen(req, timeout=self.timeout) as response:
                    data = json.loads(response.read())
                    headers = response.headers
                received = time.time()
                if isinstance(data, dict) and data.get('errorCode'):
                    raise ValueError('bitvavo_error_' + str(data['errorCode']))
                remaining = headers.get('bitvavo-ratelimit-remaining')
                reset = headers.get('bitvavo-ratelimit-resetat')
                if remaining is not None and reset is not None and float(remaining) < 40:
                    wait = max(0, float(reset) / 1000 - received + 1)
                    with self.lock:
                        self.pause_until = max(self.pause_until, time.monotonic() + wait)
                        self.metrics['rate_limit_resets_seen'] += 1
                record = {'path': path, 'params': params or {}, 'request_started_at_utc': utc(started),
                          'retrieved_at_utc': utc(received), 'server_http_date': headers.get('Date'), 'data': data}
                if path == '/time':
                    self.server_offset = data['time'] / 1000 - (started + received) / 2
                with self.lock:
                    self.records.append(record)
                    self.cache[key] = record
                    self.metrics['successful_responses'] += 1
                return copy.deepcopy(data)
            except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                code = getattr(exc, 'code', None)
                with self.lock:
                    self.errors.append({'path': path, 'attempt': attempt + 1,
                                        'error': type(exc).__name__, 'http_status': code, 'at': utc()})
                if code in {403, 429}:
                    # Respect an exchange ban/reset; do not retry rapidly or rotate IPs.
                    delay = 60.0
                    try:
                        reset = exc.headers.get('bitvavo-ratelimit-resetat')
                        retry = exc.headers.get('Retry-After')
                        delay = max(delay, float(retry or 0), float(reset or 0) / 1000 - time.time() + 1)
                    except (TypeError, ValueError):
                        pass
                    with self.lock:
                        self.pause_until = max(self.pause_until, time.monotonic() + delay)
                elif code is not None and 400 <= code < 500:
                    break
                if attempt + 1 < (retries or self.retries):
                    backoff = min(8, 2 ** attempt)
                    with self.lock:
                        self.metrics['retry_backoff_seconds'] += backoff
                    time.sleep(backoff)
        raise RuntimeError('public_api_failed:' + path)

    def metadata(self, path, params=None):
        return self.cache.get(self.key(path, params), {})

    def diagnostics(self):
        """Return additive transport telemetry without changing request behavior."""
        with self.lock:
            http_status_counts = {}
            error_type_counts = {}
            error_path_counts = {}
            for row in self.errors:
                status = row.get('http_status')
                status_key = 'NONE' if status is None else str(status)
                http_status_counts[status_key] = http_status_counts.get(status_key, 0) + 1
                error_type = row.get('error') or 'UNKNOWN'
                error_type_counts[error_type] = error_type_counts.get(error_type, 0) + 1
                path = row.get('path') or 'UNKNOWN'
                error_path_counts[path] = error_path_counts.get(path, 0) + 1
            return {
                **self.metrics,
                'pace_wait_seconds': round(self.metrics['pace_wait_seconds'], 6),
                'rate_limit_wait_seconds': round(self.metrics['rate_limit_wait_seconds'], 6),
                'retry_backoff_seconds': round(self.metrics['retry_backoff_seconds'], 6),
                'record_count': len(self.records),
                'error_attempt_count': len(self.errors),
                'http_status_counts': dict(sorted(http_status_counts.items())),
                'error_type_counts': dict(sorted(error_type_counts.items())),
                'error_path_counts': dict(sorted(error_path_counts.items())),
            }


class ReplayClient:
    """No network fallback: a missing historical input makes replay unavailable."""
    def __init__(self, records):
        self.records = records
        self.cache = {PublicClient.key(r['path'], r['params']): r for r in records}

    def get(self, path, params=None, **_):
        key = PublicClient.key(path, params)
        if key not in self.cache:
            raise RuntimeError('replay_input_missing:' + key)
        return copy.deepcopy(self.cache[key]['data'])
