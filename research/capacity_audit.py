"""Opt-in observation, never imported by production acquisition or policies.

Endpoint weights checked against official Bitvavo REST docs on 2026-09-17.
Client-start rolling windows differ from the exchange's reset-based windows.
"""
from collections import Counter
from contextlib import contextmanager
import threading
import time
import urllib.parse
import urllib.request
from unittest.mock import patch
from research.http import PublicClient

HEADERS = ('bitvavo-ratelimit-limit', 'bitvavo-ratelimit-remaining',
           'bitvavo-ratelimit-resetat', 'bitvavo-ratelimit-reset', 'retry-after', 'date')


from research.api_budget import weight


def rolling_peak(attempts, seconds=60):
    rows = sorted(attempts, key=lambda r: r['started_epoch'])
    left = total = peak = count = 0
    at = None
    for right, row in enumerate(rows):
        total += row['weight']
        while rows[left]['started_epoch'] <= row['started_epoch'] - seconds:
            total -= rows[left]['weight']
            left += 1
        if total > peak:
            peak, at = total, row['started_epoch']
        count = max(count, right-left+1)
    return {'weight': peak, 'requests': count, 'window_ending_epoch': at}


class Audit:
    def __init__(self):
        self.attempts, self.calls, self.waits = [], [], []
        self.lock, self.local = threading.Lock(), threading.local()
        self.sequence, self.callback_seconds = 0, 0.

    def append(self, target, item):
        began = time.perf_counter()
        with self.lock:
            target.append(item)
            self.callback_seconds += time.perf_counter()-began

    @contextmanager
    def observe(self):
        original_open, original_response, original_pace = urllib.request.urlopen, PublicClient._response, PublicClient.pace
        audit = self

        def opened(request, *args, **kwargs):
            url = urllib.parse.urlsplit(request.full_url)
            if url.scheme != 'https' or url.netloc != 'api.bitvavo.com' or request.get_method() != 'GET':
                raise ValueError('AUDIT_PUBLIC_GET_ONLY')
            if any(k.lower().startswith('bitvavo-access') for k in request.headers):
                raise ValueError('AUDIT_NO_PRIVATE_AUTH')
            path = url.path.removeprefix('/v2')
            params = dict(urllib.parse.parse_qsl(url.query))
            row = {'call_id': getattr(audit.local, 'call_id', None), 'path': path, 'params': params,
                   'worker': threading.current_thread().name,
                   'started_epoch': time.time(), 'weight': weight(path, params),
                   'timeout_seconds': kwargs.get('timeout'), 'status': None, 'error': None, 'headers': {}}
            began = time.monotonic()
            try:
                response = original_open(request, *args, **kwargs)
            except Exception as exc:
                row.update(status=getattr(exc, 'code', None), error=type(exc).__name__,
                           timeout=isinstance(exc, TimeoutError) or isinstance(getattr(exc, 'reason', None), TimeoutError))
                headers = getattr(exc, 'headers', {}) or {}
                row['headers'] = {h: headers.get(h) for h in HEADERS if headers.get(h) is not None}
                row.update(finished_epoch=time.time(), elapsed_seconds=time.monotonic()-began)
                audit.append(audit.attempts, row)
                raise
            row['status'] = response.status
            row['headers'] = {h: response.headers.get(h) for h in HEADERS if response.headers.get(h) is not None}

            class Response:
                headers = response.headers
                def __enter__(self):
                    return self
                def read(self, *a, **kw):
                    try:
                        data = response.read(*a, **kw)
                        row['bytes'] = row.get('bytes', 0)+len(data)
                        return data
                    except Exception as exc:
                        row.update(error=type(exc).__name__, timeout=isinstance(exc, TimeoutError))
                        raise
                def __exit__(self, *a):
                    try:
                        response.close()
                    finally:
                        row.update(finished_epoch=time.time(), elapsed_seconds=time.monotonic()-began)
                        audit.append(audit.attempts, row)
            return Response()

        def response(client, path, params=None, retries=None, cache=True, deadline=None):
            with audit.lock:
                audit.sequence += 1
                call_id = audit.sequence
            audit.local.call_id = call_id
            row = {'id': call_id, 'path': path, 'params': params or {}, 'cache_allowed': cache,
                   'started_epoch': time.time(), 'deadline_remaining_seconds': None if deadline is None else deadline-time.monotonic()}
            began = time.monotonic()
            try:
                value = original_response(client, path, params, retries, cache, deadline)
                row['response_id'] = value['response_id']
                return value
            except Exception as exc:
                row.update(error=type(exc).__name__, reason=str(exc))
                raise
            finally:
                row.update(finished_epoch=time.time(), elapsed_seconds=time.monotonic()-began)
                audit.append(audit.calls, row)
                audit.local.call_id = None

        def pace(client, deadline=None):
            began = time.monotonic()
            row = {'call_id': getattr(audit.local, 'call_id', None), 'started_epoch': time.time(),
                   'pause_remaining_seconds': max(0., client.pause_until-began)}
            try:
                return original_pace(client, deadline)
            except Exception as exc:
                row['error'] = str(exc)
                raise
            finally:
                row['elapsed_seconds'] = time.monotonic()-began
                audit.append(audit.waits, row)

        with patch.object(urllib.request, 'urlopen', opened), patch.object(PublicClient, '_response', response), patch.object(PublicClient, 'pace', pace):
            yield self

    def result(self):
        counts = Counter(a['call_id'] for a in self.attempts)
        return {'schema_version': 1, 'purpose': 'PUBLIC_CAPACITY_AUDIT_NOT_PILOT',
                'attempts': sorted(self.attempts, key=lambda a: a['started_epoch']), 'logical_calls': self.calls,
                'pacing_waits': self.waits, 'observer_append_seconds': self.callback_seconds,
                'summary': {'http_attempts': len(self.attempts), 'weight_total': sum(a['weight'] for a in self.attempts),
                    'rolling_60s_peak': rolling_peak(self.attempts), 'retry_attempts': sum(max(0,n-1) for n in counts.values()),
                    'timeouts': sum(bool(a.get('timeout')) for a in self.attempts),
                    'http_429': sum(a['status']==429 for a in self.attempts),
                    'cache_only_calls': sum(c['id'] not in counts and 'response_id' in c for c in self.calls),
                    'pace_thread_seconds': sum(w['elapsed_seconds'] for w in self.waits)}}
