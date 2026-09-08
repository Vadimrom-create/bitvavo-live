"""Minimal GET-only account adapter; no private payload enters public replay."""
from __future__ import annotations

import hashlib
import hmac
import json
import time
import urllib.request

from research.common import finite, utc


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise RuntimeError('PRIVATE_REDIRECT_REFUSED')


class ReadOnlyAccount:
    ALLOWED = {'/balance', '/ordersOpen'}

    def __init__(self, key, secret):
        if not key or not secret:
            raise ValueError('READ_CREDENTIALS_MISSING')
        self.key, self.secret = key, secret
        self.opener = urllib.request.build_opener(NoRedirect())

    def get(self, endpoint):
        if endpoint not in self.ALLOWED:
            raise PermissionError('PRIVATE_ENDPOINT_NOT_ALLOWED')
        ts = str(int(time.time() * 1000))
        path = '/v2' + endpoint
        signature = hmac.new(self.secret.encode(), (ts + 'GET' + path).encode(), hashlib.sha256).hexdigest()
        request = urllib.request.Request('https://api.bitvavo.com' + path, method='GET', headers={
            'Bitvavo-Access-Key': self.key, 'Bitvavo-Access-Timestamp': ts,
            'Bitvavo-Access-Signature': signature, 'Bitvavo-Access-Window': '10000',
            'Accept': 'application/json'})
        try:
            with self.opener.open(request, timeout=12) as response:
                result = json.loads(response.read())
            if not isinstance(result, list):
                raise ValueError('INVALID_ACCOUNT_RESPONSE')
            return result
        except Exception:
            # Never include a request, account response, headers or secrets.
            raise RuntimeError('PRIVATE_ACCOUNT_READ_FAILED') from None

    def snapshot(self):
        balances = self.get('/balance')
        retrieved = utc()
        orders = self.get('/ordersOpen')
        normalized = []
        for row in balances:
            available, locked = finite(row.get('available')), finite(row.get('inOrder'))
            symbol = row.get('symbol')
            if not isinstance(symbol, str) or available is None or locked is None or min(available, locked) < 0:
                raise ValueError('INVALID_BALANCE')
            normalized.append({'symbol': symbol, 'available': available, 'in_order': locked,
                               'amount': available + locked})
        return {'retrieved_at_utc': retrieved, 'balances': normalized, 'orders': orders}
