"""Strict view-only Bitvavo account adapter; no private payload enters public replay.

Only read-only account endpoints are permitted. Open-order/trade endpoints
require trading permission on Bitvavo and remain intentionally unavailable.
Balance plus account transaction history are enough to reconstruct current
position cost basis without granting trading rights.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import time
import urllib.parse
import urllib.request

from research.common import finite, utc


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise RuntimeError('PRIVATE_REDIRECT_REFUSED')


class ReadOnlyAccount:
    ALLOWED = {'/balance', '/account/history'}
    ACCESS_MODE = 'VIEW_ONLY_BALANCE_AND_TRANSACTIONS'
    OPEN_ORDERS_VISIBILITY = 'UNAVAILABLE_VIEW_ONLY'

    def __init__(self, key, secret):
        if not key or not secret:
            raise ValueError('READ_CREDENTIALS_MISSING')
        self.key, self.secret = key, secret
        self.opener = urllib.request.build_opener(NoRedirect())

    def get(self, endpoint, params=None):
        if endpoint not in self.ALLOWED:
            raise PermissionError('PRIVATE_ENDPOINT_NOT_ALLOWED')
        query = urllib.parse.urlencode(params or {})
        ts = str(int(time.time() * 1000))
        path = '/v2' + endpoint + (('?' + query) if query else '')
        signature = hmac.new(self.secret.encode(), (ts + 'GET' + path).encode(), hashlib.sha256).hexdigest()
        request = urllib.request.Request('https://api.bitvavo.com' + path, method='GET', headers={
            'Bitvavo-Access-Key': self.key, 'Bitvavo-Access-Timestamp': ts,
            'Bitvavo-Access-Signature': signature, 'Bitvavo-Access-Window': '10000',
            'Accept': 'application/json'})
        try:
            with self.opener.open(request, timeout=12) as response:
                return json.loads(response.read())
        except Exception:
            # Never include a request, account response, headers or secrets.
            raise RuntimeError('PRIVATE_ACCOUNT_READ_FAILED') from None

    def transaction_history(self, *, from_date=None, to_date=None, max_pages=50):
        """Read account buy/sell transactions without enabling trade permission."""
        merged = []
        page = 1
        while page <= max_pages:
            params = {'page': page, 'maxItems': 100}
            if from_date is not None:
                params['fromDate'] = int(from_date)
            if to_date is not None:
                params['toDate'] = int(to_date)
            payload = self.get('/account/history', params)
            if not isinstance(payload, dict) or not isinstance(payload.get('items'), list):
                raise ValueError('INVALID_TRANSACTION_HISTORY_RESPONSE')
            merged.extend(payload['items'])
            total_pages = int(payload.get('totalPages') or 1)
            if page >= total_pages:
                return merged
            page += 1
        raise RuntimeError('TRANSACTION_HISTORY_PAGE_LIMIT_REACHED')

    def snapshot(self):
        balances = self.get('/balance')
        if not isinstance(balances, list):
            raise ValueError('INVALID_ACCOUNT_RESPONSE')
        retrieved = utc()
        normalized = []
        for row in balances:
            available, locked = finite(row.get('available')), finite(row.get('inOrder'))
            symbol = row.get('symbol')
            if not isinstance(symbol, str) or available is None or locked is None or min(available, locked) < 0:
                raise ValueError('INVALID_BALANCE')
            normalized.append({'symbol': symbol, 'available': available, 'in_order': locked,
                               'amount': available + locked})
        return {
            'retrieved_at_utc': retrieved,
            'balances': normalized,
            'access_mode': self.ACCESS_MODE,
            'open_orders_visibility': self.OPEN_ORDERS_VISIBILITY,
        }
