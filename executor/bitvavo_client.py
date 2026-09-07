#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import hmac
import json
import time
import urllib.parse
from typing import Any

import requests


class BitvavoError(RuntimeError):
    pass


class BitvavoClient:
    """Minimal Bitvavo REST client for the private executor.

    The API key is expected to have only View + Trade permissions, never Withdraw.
    """

    def __init__(self, api_key: str, api_secret: str, operator_id: int, access_window: int = 10_000):
        self.api_key = api_key.strip()
        self.api_secret = api_secret.strip()
        self.operator_id = int(operator_id)
        self.access_window = int(access_window)
        self.base = "https://api.bitvavo.com"
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json", "User-Agent": "bitvavo-private-executor/1.0"})

    def _signature(self, timestamp: int, method: str, path_with_query: str, body_text: str = "") -> str:
        payload = f"{timestamp}{method.upper()}{path_with_query}{body_text}"
        return hmac.new(self.api_secret.encode(), payload.encode(), hashlib.sha256).hexdigest()

    def request(self, method: str, endpoint: str, params: dict[str, Any] | None = None,
                body: dict[str, Any] | None = None, private: bool = True,
                timeout: float = 15.0) -> Any:
        method = method.upper()
        path = "/v2" + endpoint
        query = urllib.parse.urlencode(params or {}, doseq=True)
        path_with_query = path + ("?" + query if query else "")
        url = self.base + path_with_query
        body_text = "" if method == "GET" or body is None else json.dumps(body, separators=(",", ":"))
        headers = {"Content-Type": "application/json"}

        if private:
            ts = int(time.time() * 1000)
            headers.update({
                "Bitvavo-Access-Key": self.api_key,
                "Bitvavo-Access-Timestamp": str(ts),
                "Bitvavo-Access-Window": str(self.access_window),
                "Bitvavo-Access-Signature": self._signature(ts, method, path_with_query, body_text),
            })

        response = self.session.request(method, url, headers=headers, data=(body_text or None), timeout=timeout)
        try:
            data = response.json()
        except Exception:
            data = response.text
        if response.status_code >= 400:
            raise BitvavoError(f"HTTP {response.status_code}: {data}")
        if isinstance(data, dict) and data.get("errorCode"):
            raise BitvavoError(f"Bitvavo {data.get('errorCode')}: {data.get('error')}")
        return data

    # Private account state
    def balances(self):
        return self.request("GET", "/balance")

    def open_orders(self, market: str | None = None):
        params = {"market": market} if market else None
        return self.request("GET", "/ordersOpen", params=params)

    def order(self, market: str, order_id: str | None = None, client_order_id: str | None = None):
        params: dict[str, Any] = {"market": market}
        if client_order_id:
            params["clientOrderId"] = client_order_id
        elif order_id:
            params["orderId"] = order_id
        else:
            raise ValueError("order_id or client_order_id required")
        return self.request("GET", "/order", params=params)

    def trade_history(self, market: str | None = None, limit: int = 100):
        params: dict[str, Any] = {"limit": limit}
        if market:
            params["market"] = market
        return self.request("GET", "/trades", params=params)

    # Trading
    def create_order(self, *, market: str, side: str, order_type: str,
                     client_order_id: str, amount: str | None = None,
                     amount_quote: str | None = None, price: str | None = None,
                     trigger_amount: str | None = None,
                     trigger_reference: str = "lastTrade",
                     time_in_force: str = "GTC", post_only: bool = False,
                     cod_group_id: int | None = None):
        body: dict[str, Any] = {
            "market": market,
            "side": side,
            "orderType": order_type,
            "operatorId": self.operator_id,
            "clientOrderId": client_order_id,
            "timeInForce": time_in_force,
            "postOnly": bool(post_only),
            "responseRequired": True,
        }
        if amount is not None:
            body["amount"] = str(amount)
        if amount_quote is not None:
            body["amountQuote"] = str(amount_quote)
        if price is not None:
            body["price"] = str(price)
        if trigger_amount is not None:
            body.update({
                "triggerAmount": str(trigger_amount),
                "triggerType": "price",
                "triggerReference": trigger_reference,
            })
        if cod_group_id is not None:
            body["codGroupId"] = int(cod_group_id)
        return self.request("POST", "/order", body=body)

    def cancel_order(self, *, market: str, order_id: str | None = None,
                     client_order_id: str | None = None):
        params: dict[str, Any] = {"market": market, "operatorId": self.operator_id}
        if client_order_id:
            params["clientOrderId"] = client_order_id
        elif order_id:
            params["orderId"] = order_id
        else:
            raise ValueError("order_id or client_order_id required")
        return self.request("DELETE", "/order", params=params)

    def cancel_all(self, market: str | None = None):
        params: dict[str, Any] = {"operatorId": self.operator_id}
        if market:
            params["market"] = market
        return self.request("DELETE", "/orders", params=params)

    def cancel_orders_after(self, cod_group_id: int, expiry_after_seconds: int = 30):
        return self.request("POST", "/cancelOrdersAfter", body={
            "codGroupId": int(cod_group_id),
            "expiryAfterSeconds": int(expiry_after_seconds),
        })

    # Public validation
    def ticker_book(self, market: str):
        return self.request("GET", "/ticker/book", params={"market": market}, private=False)

    def order_book(self, market: str, depth: int = 100):
        return self.request("GET", f"/{market}/book", params={"depth": depth}, private=False)

    def markets(self):
        return self.request("GET", "/markets", private=False)
