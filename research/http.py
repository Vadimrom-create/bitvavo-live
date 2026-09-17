"""Public-only transport, bounded retries, shared rate limiting and replay log."""
from __future__ import annotations

import copy
import hashlib
import json
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

from research.common import utc, timestamp
from research.api_budget import WeightedBudget, weight


class PublicClient:
    def __init__(self, timeout=12, retries=3, requests_per_second=12, *, budget=None, max_elapsed_seconds=300):
        self.budget = budget if budget is not None else WeightedBudget()
        self.collection_deadline = time.monotonic() + max_elapsed_seconds
        self.budget_wait_seconds = 0.0
        self.timeout, self.retries = timeout, retries
        self.spacing = 1 / requests_per_second
        self.lock = threading.Lock()
        self.next_request = 0.0
        self.pause_until = 0.0
        self.records = []
        self.cache = {}
        self.consumptions = []
        self.request_sequence = 0
        self.clock_uncertainty_seconds = 30.0
        self.consumer_sequences = {}
        self.errors = []
        self.server_offset = 0.0

    @staticmethod
    def key(path, params):
        return path + '?' + urllib.parse.urlencode(sorted((params or {}).items()))

    def pace(self, deadline=None):
        deadline = min(self.collection_deadline, deadline if deadline is not None else float('inf'))
        with self.lock:
            now = time.monotonic()
            scheduled = max(now, self.next_request, self.pause_until)
            if deadline is not None and scheduled >= deadline:
                raise RuntimeError('OPTIONAL_COLLECTION_DEADLINE')
            self.next_request = scheduled + self.spacing
        delay = scheduled - now
        if delay > 0:
            time.sleep(delay)

    def _response(self, path, params=None, retries=None, cache=True, deadline=None):
        if not (path in {'/time', '/markets', '/ticker/24h', '/ticker/book', '/ticker/price'}
                or re.fullmatch(r'/[A-Z0-9]+-EUR/(candles|book|trades)', path)):
            raise ValueError('public_endpoint_not_allowed')
        key = self.key(path, params)
        with self.lock:
            cached = self.cache.get(key) if cache else None
        if cached is not None:
            return cached
        effective_deadline = min(self.collection_deadline, deadline if deadline is not None else float('inf'))
        reason = ('COLLECTION_FRESHNESS_DEADLINE' if effective_deadline == self.collection_deadline
                  else 'OPTIONAL_COLLECTION_DEADLINE')
        def expired(cause=None):
            with self.lock:
                self.errors.append({'path':path, 'params':params or {}, 'error':reason, 'cause':cause, 'at':utc()})
            raise RuntimeError(reason)
        for attempt in range(retries or self.retries):
            if time.monotonic() >= effective_deadline: expired()
            try:
                self.pace() if deadline is None else self.pace(effective_deadline)
                waited = self.budget.reserve(weight(path, params), effective_deadline)
                with self.lock: self.budget_wait_seconds += waited
            except RuntimeError as exc:
                expired(str(exc))
            if time.monotonic() >= effective_deadline: expired()
            started = time.time()
            with self.lock:
                self.request_sequence += 1
                request_id = self.request_sequence
            try:
                req = urllib.request.Request('https://api.bitvavo.com/v2' + key,
                    headers={'Accept': 'application/json', 'User-Agent': 'bitvavo-observatory/5.0'})
                timeout = min(self.timeout, max(.001,effective_deadline-time.monotonic()))
                with urllib.request.urlopen(req, timeout=timeout) as response:
                    data = json.loads(response.read())
                    headers = response.headers
                received = time.time()
                if isinstance(data, dict) and data.get('errorCode'):
                    raise ValueError('bitvavo_error_' + str(data['errorCode']))
                self.budget.observe(headers, now=received)
                if time.monotonic() >= effective_deadline: expired()
                record = {'path': path, 'params': params or {}, 'request_started_at_utc': utc(started),
                          'retrieved_at_utc': utc(received), 'server_http_date': headers.get('Date'), 'data': data,
                          'request_id': request_id, 'server_offset_seconds': self.server_offset,
                          'clock_uncertainty_seconds': self.clock_uncertainty_seconds,
                          'market_asof_at_utc': None}
                if path == '/time':
                    self.server_offset = data['time'] / 1000 - (started + received) / 2
                    self.clock_uncertainty_seconds = (received-started)/2 + .001
                record['response_id'] = hashlib.sha256(json.dumps(record, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
                with self.lock:
                    self.records.append(record)
                    self.cache[key] = record
                return record
            except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                code = getattr(exc, 'code', None)
                with self.lock:
                    self.errors.append({'path': path, 'attempt': attempt + 1,
                                        'error': type(exc).__name__, 'http_status': code, 'at': utc()})
                self.budget.observe(getattr(exc, 'headers', {}) or {}, status=code)
                if code in {403, 429}:
                    # Shared cooldown is persisted before failing this logical call.
                    break
                if code is not None and 400 <= code < 500:
                    break
                if time.monotonic() >= effective_deadline: expired(type(exc).__name__)
                if attempt + 1 < (retries or self.retries):
                    delay=min(8, 2 ** attempt)
                    if time.monotonic()+delay >= effective_deadline: expired()
                    time.sleep(delay)
        raise RuntimeError('public_api_failed:' + path)

    def capture(self, path, params=None, retries=None, cache=True, *, consumer_id='legacy', cutoff=None, deadline=None):
        record = self._response(path, params, retries, cache) if deadline is None else self._response(path, params, retries, cache, deadline)
        if cutoff is not None and timestamp(record['retrieved_at_utc']) > timestamp(cutoff):
            raise ValueError('INPUT_NOT_AVAILABLE_AT_CUTOFF')
        key = self.key(path, params)
        with self.lock:
            identity = (consumer_id, key)
            seq = self.consumer_sequences.get(identity, 0)
            self.consumer_sequences[identity] = seq + 1
            self.consumptions.append({'consumer_id': consumer_id, 'key': key, 'sequence': seq,
                                      'response_id': record['response_id'], 'consumed_at_utc': utc(),
                                      'availability_cutoff': cutoff})
        return copy.deepcopy(record)

    def get(self, path, params=None, retries=None, cache=True, **kwargs):
        return self.capture(path, params, retries, cache, **kwargs)['data']

    def metadata(self, path, params=None):
        # Compatibility only; new consumers must use capture for an atomic binding.
        with self.lock:
            return copy.deepcopy(self.cache.get(self.key(path, params), {}))


class ReplayClient:
    """No network fallback. Legacy logs retain their original reading convention."""
    def __init__(self, records, consumptions=None, consumer_id='v4'):
        self.records = records
        self.cache = {PublicClient.key(r['path'], r['params']): r for r in records}
        self.by_id = {r['response_id']: r for r in records if 'response_id' in r}
        self.consumptions = consumptions
        self.consumer_id = consumer_id
        self.positions = {}
        self.bound = {}
        self.server_offset = 0.
        self.clock_uncertainty_seconds = 30.

    def capture(self, path, params=None, *, consumer_id=None, cutoff=None, **_):
        key = PublicClient.key(path, params)
        if self.consumptions is None:
            if key not in self.cache:
                raise RuntimeError('replay_input_missing:' + key)
            record = self.cache[key]
        else:
            identity = (consumer_id or self.consumer_id, key)
            matches = sorted((c for c in self.consumptions if (c['consumer_id'], c['key']) == identity),
                             key=lambda c: c['sequence'])
            pos = self.positions.get(identity, 0)
            if pos >= len(matches):
                raise RuntimeError('replay_consumption_missing:' + str(identity))
            record = self.by_id[matches[pos]['response_id']]
            self.positions[identity] = pos + 1
        if cutoff is not None and timestamp(record['retrieved_at_utc']) > timestamp(cutoff):
            raise ValueError('INPUT_NOT_AVAILABLE_AT_CUTOFF')
        self.bound[key] = record
        return copy.deepcopy(record)

    def get(self, path, params=None, **kwargs):
        return self.capture(path, params, **kwargs)['data']

    def metadata(self, path, params=None):
        return copy.deepcopy(self.bound.get(PublicClient.key(path, params), {}))
