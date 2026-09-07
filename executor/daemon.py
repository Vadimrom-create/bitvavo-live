#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import threading
import time
import uuid
from datetime import datetime, timezone
from decimal import Decimal, ROUND_DOWN
from pathlib import Path
from typing import Any

import requests
import websocket

from bitvavo_client import BitvavoClient, BitvavoError


def env_bool(name: str, default: bool = False) -> bool:
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def iso_now() -> str:
    return utcnow().isoformat()


def parse_iso(s: str) -> datetime:
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return datetime.fromisoformat(s).astimezone(timezone.utc)


def atomic_json(path: Path, data: dict[str, Any]) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


class Executor:
    def __init__(self):
        self.api_key = os.environ["BITVAVO_API_KEY"]
        self.api_secret = os.environ["BITVAVO_API_SECRET"]
        self.operator_id = int(os.getenv("BITVAVO_OPERATOR_ID", "26090701"))
        self.dry_run = env_bool("DRY_RUN", True)
        self.max_order_eur = Decimal(os.getenv("MAX_ORDER_EUR", "600"))
        self.max_total_new_exposure_eur = Decimal(os.getenv("MAX_TOTAL_NEW_EXPOSURE_EUR", "1200"))
        self.max_entry_price_drift_pct = Decimal(os.getenv("MAX_ENTRY_PRICE_DRIFT_PCT", "0.50"))
        self.max_spread_pct = Decimal(os.getenv("MAX_SPREAD_PCT", "0.60"))
        self.approval_max_age = int(os.getenv("APPROVAL_MAX_AGE_SECONDS", "600"))
        self.approval_url = os.getenv(
            "APPROVAL_URL",
            "https://raw.githubusercontent.com/Vadimrom-create/bitvavo-live/main/trade_approval.json",
        )
        self.poll_seconds = float(os.getenv("POLL_SECONDS", "4"))
        self.auto_cancel_unknown = env_bool("AUTO_CANCEL_UNKNOWN_ORDERS", False)
        self.freeze_on_unknown = env_bool("SECURITY_FREEZE_ON_UNKNOWN", True)
        self.github_token = os.getenv("GITHUB_STATUS_TOKEN", "").strip()
        self.github_repo = os.getenv("GITHUB_STATUS_REPO", "Vadimrom-create/bitvavo-live")

        self.state_dir = Path(os.getenv("STATE_DIR", "/var/lib/bitvavo-executor"))
        self.state_dir.mkdir(parents=True, exist_ok=True)
        self.state_file = self.state_dir / "state.json"
        self.event_log = self.state_dir / "events.jsonl"

        self.client = BitvavoClient(self.api_key, self.api_secret, self.operator_id)
        self.lock = threading.RLock()
        self.state = self._load_state()
        self.market_meta = self._load_market_meta()
        self.stop_event = threading.Event()

    def _load_state(self) -> dict[str, Any]:
        default = {
            "version": 1,
            "security_freeze": False,
            "seen_approval_ids": [],
            "authorized_client_order_ids": [],
            "orders": {},
            "last_security_event": None,
            "last_approval_result": None,
            "started_at_utc": iso_now(),
        }
        if self.state_file.exists():
            try:
                loaded = json.loads(self.state_file.read_text(encoding="utf-8"))
                default.update(loaded)
            except Exception:
                pass
        return default

    def _save_state(self):
        with self.lock:
            atomic_json(self.state_file, self.state)

    def _load_market_meta(self) -> dict[str, dict[str, Any]]:
        rows = self.client.markets()
        return {r.get("market"): r for r in rows if isinstance(r, dict) and r.get("market")}

    def _event(self, kind: str, **payload):
        row = {"ts_utc": iso_now(), "kind": kind, **payload}
        with self.event_log.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(json.dumps(row, ensure_ascii=False), flush=True)
        return row

    def _publish_github_json(self, path: str, payload: dict[str, Any], message: str):
        if not self.github_token:
            return
        api = f"https://api.github.com/repos/{self.github_repo}/contents/{path}"
        headers = {
            "Authorization": f"Bearer {self.github_token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "bitvavo-private-executor/1.0",
        }
        sha = None
        r = requests.get(api, headers=headers, timeout=10)
        if r.status_code == 200:
            sha = r.json().get("sha")
        body = {
            "message": message,
            "content": base64.b64encode((json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode()).decode(),
            "branch": "main",
        }
        if sha:
            body["sha"] = sha
        r = requests.put(api, headers=headers, json=body, timeout=15)
        if r.status_code not in (200, 201):
            self._event("github_publish_error", path=path, status=r.status_code, response=r.text[:500])

    def publish_status(self):
        with self.lock:
            safe = {
                "generated_at_utc": iso_now(),
                "online": True,
                "dry_run": self.dry_run,
                "operator_id": self.operator_id,
                "security_freeze": bool(self.state.get("security_freeze")),
                "auto_cancel_unknown_orders": self.auto_cancel_unknown,
                "last_security_event": self.state.get("last_security_event"),
                "last_approval_result": self.state.get("last_approval_result"),
                "authorized_open_order_count": sum(
                    1 for v in self.state.get("orders", {}).values()
                    if v.get("status") not in {"filled", "canceled", "expired", "rejected"}
                ),
                "note": "Sanitized status only. No API keys, balances or private wallet holdings are published.",
            }
        self._publish_github_json("executor_status.json", safe, "Update private executor status")

    def security_event(self, reason: str, event: dict[str, Any]):
        safe_event = {
            "event_id": str(uuid.uuid4()),
            "detected_at_utc": iso_now(),
            "severity": "CRITICAL",
            "reason": reason,
            "market": event.get("market"),
            "event": event.get("event"),
            "orderId": event.get("orderId"),
            "clientOrderId": event.get("clientOrderId"),
            "operatorId": event.get("operatorId"),
            "side": event.get("side"),
            "orderType": event.get("orderType"),
            "status": event.get("status"),
            "action_taken": [],
        }
        if self.freeze_on_unknown:
            with self.lock:
                self.state["security_freeze"] = True
            safe_event["action_taken"].append("SECURITY_FREEZE")

        if self.auto_cancel_unknown and event.get("event") == "order" and event.get("status") in {
            "new", "awaitingTrigger", "partiallyFilled"
        }:
            try:
                self.client.cancel_order(market=event["market"], order_id=event.get("orderId"))
                safe_event["action_taken"].append("CANCEL_UNKNOWN_ORDER")
            except Exception as exc:
                safe_event["action_taken"].append(f"CANCEL_FAILED:{type(exc).__name__}")

        with self.lock:
            self.state["last_security_event"] = safe_event
        self._save_state()
        self._event("SECURITY_EVENT", **safe_event)
        self._publish_github_json("security_event.json", safe_event, "SECURITY: unknown Bitvavo activity detected")
        self.publish_status()

    def is_authorized_event(self, event: dict[str, Any]) -> bool:
        op = event.get("operatorId")
        cid = event.get("clientOrderId")
        with self.lock:
            authorized = set(self.state.get("authorized_client_order_ids", []))
        return int(op) == self.operator_id and bool(cid) and cid in authorized if op is not None else False

    def handle_account_event(self, event: dict[str, Any]):
        if event.get("event") not in {"order", "fill"}:
            return
        if not self.is_authorized_event(event):
            self.security_event("UNKNOWN_OR_UNAUTHORIZED_BITVAVO_ACTIVITY", event)
            return
        cid = event.get("clientOrderId")
        with self.lock:
            order = self.state.setdefault("orders", {}).setdefault(cid, {})
            order.update({
                "last_event_utc": iso_now(),
                "market": event.get("market"),
                "orderId": event.get("orderId"),
                "status": event.get("status", order.get("status")),
                "event": event.get("event"),
                "operatorId": event.get("operatorId"),
            })
            if event.get("event") == "fill":
                order.setdefault("fills", []).append({
                    "fillId": event.get("fillId"),
                    "timestamp": event.get("timestamp"),
                    "amount": event.get("amount"),
                    "price": event.get("price"),
                    "side": event.get("side"),
                    "fee": event.get("fee"),
                    "feeCurrency": event.get("feeCurrency"),
                })
        self._save_state()
        self._event("authorized_account_event", market=event.get("market"), event=event.get("event"), clientOrderId=cid)

    def websocket_loop(self):
        endpoint = "wss://ws.bitvavo.com/v2/"
        while not self.stop_event.is_set():
            ws = None
            try:
                ws = websocket.create_connection(endpoint, timeout=30)
                ts = int(time.time() * 1000)
                payload = f"{ts}GET/v2/websocket"
                sig = hmac.new(self.api_secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
                ws.send(json.dumps({
                    "action": "authenticate",
                    "key": self.api_key,
                    "signature": sig,
                    "timestamp": ts,
                    "window": 10_000,
                }))
                authenticated = False
                subscribed = False
                last_ping = time.time()
                while not self.stop_event.is_set():
                    ws.settimeout(5)
                    try:
                        raw = ws.recv()
                    except Exception:
                        raw = None
                    if raw:
                        msg = json.loads(raw)
                        if msg.get("event") == "authenticate" and msg.get("authenticated") is True:
                            authenticated = True
                        if authenticated and not subscribed:
                            ws.send(json.dumps({
                                "action": "subscribe",
                                "channels": [{"name": "account", "markets": "*"}],
                            }))
                            subscribed = True
                            self._event("websocket_account_subscribed")
                        self.handle_account_event(msg)
                    if time.time() - last_ping > 20:
                        ws.ping()
                        last_ping = time.time()
            except Exception as exc:
                self._event("websocket_reconnect", error=f"{type(exc).__name__}:{exc}")
                time.sleep(3)
            finally:
                try:
                    if ws:
                        ws.close()
                except Exception:
                    pass

    def fetch_approval(self) -> dict[str, Any] | None:
        r = requests.get(self.approval_url, headers={"Cache-Control": "no-cache"}, timeout=10)
        r.raise_for_status()
        data = r.json()
        approval = data.get("approval") if isinstance(data, dict) else None
        return approval if isinstance(approval, dict) else None

    def _decimal_step_down(self, value: Decimal, decimals: int) -> Decimal:
        quantum = Decimal(1).scaleb(-int(decimals))
        return value.quantize(quantum, rounding=ROUND_DOWN)

    def validate_approval(self, a: dict[str, Any]) -> tuple[bool, str, dict[str, Any]]:
        required = {"id", "status", "created_at_utc", "expires_at_utc", "market", "side", "order_type", "stake_eur", "reference_price"}
        missing = sorted(required - set(a))
        if missing:
            return False, f"missing_fields:{','.join(missing)}", {}
        if a.get("status") != "APPROVED_BY_USER":
            return False, "status_not_approved", {}
        if a.get("side") != "buy":
            return False, "phase1_allows_buy_approvals_only", {}
        if a.get("order_type") != "limit":
            return False, "phase1_allows_limit_entries_only", {}
        market = str(a["market"])
        if market not in self.market_meta or not market.endswith("-EUR"):
            return False, "unknown_or_non_eur_market", {}
        stake = Decimal(str(a["stake_eur"]))
        if stake <= 0 or stake > self.max_order_eur:
            return False, "stake_outside_guardrail", {}
        created = parse_iso(str(a["created_at_utc"]))
        expires = parse_iso(str(a["expires_at_utc"]))
        age = (utcnow() - created).total_seconds()
        if age < -30 or age > self.approval_max_age or utcnow() > expires:
            return False, "approval_stale_or_expired", {}
        with self.lock:
            if self.state.get("security_freeze"):
                return False, "security_freeze_active", {}
            if a["id"] in self.state.get("seen_approval_ids", []):
                return False, "already_seen", {}

        book = self.client.ticker_book(market)
        best_bid = Decimal(str(book.get("bid")))
        best_ask = Decimal(str(book.get("ask")))
        mid = (best_bid + best_ask) / 2
        spread_pct = (best_ask - best_bid) / mid * 100
        if spread_pct > self.max_spread_pct:
            return False, f"spread_too_wide:{spread_pct:.4f}%", {}

        limit_price = Decimal(str(a.get("limit_price")))
        reference_price = Decimal(str(a.get("reference_price")))
        drift_pct = abs(mid / reference_price - 1) * 100
        if drift_pct > self.max_entry_price_drift_pct:
            return False, f"market_drifted:{drift_pct:.4f}%", {}
        if limit_price <= 0:
            return False, "invalid_limit_price", {}

        meta = self.market_meta[market]
        qdec = int(meta.get("quantityDecimals", 8))
        amount = self._decimal_step_down(stake / limit_price, qdec)
        if amount <= 0:
            return False, "rounded_amount_zero", {}

        execution_type = "IMMEDIATELY_EXECUTABLE_LIMIT" if limit_price >= best_ask else "PASSIVE_LIMIT_BELOW_MARKET"
        context = {
            "best_bid": str(best_bid),
            "best_ask": str(best_ask),
            "spread_pct": float(spread_pct),
            "drift_pct": float(drift_pct),
            "limit_price": str(limit_price),
            "amount": format(amount, "f"),
            "execution_type": execution_type,
        }
        return True, "ok", context

    def execute_approval(self, a: dict[str, Any], ctx: dict[str, Any]):
        cid = str(uuid.uuid4())
        result: dict[str, Any] = {
            "approval_id": a["id"],
            "processed_at_utc": iso_now(),
            "market": a["market"],
            "stake_eur": a["stake_eur"],
            "limit_price": ctx["limit_price"],
            "execution_type": ctx["execution_type"],
            "dry_run": self.dry_run,
        }

        with self.lock:
            self.state.setdefault("seen_approval_ids", []).append(a["id"])
            self.state["seen_approval_ids"] = self.state["seen_approval_ids"][-500:]

        if self.dry_run:
            result.update({"status": "DRY_RUN_VALIDATED", "clientOrderId": None})
            with self.lock:
                self.state["last_approval_result"] = result
            self._save_state()
            self._event("dry_run_approval_validated", **result)
            self.publish_status()
            return

        # Register the ID BEFORE the order request so the account stream cannot race the registry.
        with self.lock:
            self.state.setdefault("authorized_client_order_ids", []).append(cid)
            self.state["authorized_client_order_ids"] = self.state["authorized_client_order_ids"][-1000:]
            self.state.setdefault("orders", {})[cid] = {
                "approval_id": a["id"],
                "market": a["market"],
                "status": "SUBMITTING",
                "entry_plan": a,
                "created_at_utc": iso_now(),
            }
        self._save_state()

        try:
            response = self.client.create_order(
                market=a["market"],
                side="buy",
                order_type="limit",
                client_order_id=cid,
                amount=ctx["amount"],
                price=ctx["limit_price"],
                time_in_force="GTC",
                post_only=False,
            )
            result.update({
                "status": "ORDER_SUBMITTED",
                "clientOrderId": cid,
                "orderId": response.get("orderId") if isinstance(response, dict) else None,
            })
            with self.lock:
                self.state["orders"][cid].update({
                    "status": response.get("status", "submitted") if isinstance(response, dict) else "submitted",
                    "orderId": response.get("orderId") if isinstance(response, dict) else None,
                })
                self.state["last_approval_result"] = result
            self._save_state()
            self._event("order_submitted", **result)
            self.publish_status()
        except Exception as exc:
            result.update({"status": "ORDER_SUBMIT_FAILED", "clientOrderId": cid, "error": f"{type(exc).__name__}:{exc}"})
            with self.lock:
                self.state["orders"][cid]["status"] = "SUBMIT_FAILED"
                self.state["last_approval_result"] = result
            self._save_state()
            self._event("order_submit_failed", **result)
            self.publish_status()

    def approval_loop(self):
        while not self.stop_event.is_set():
            try:
                approval = self.fetch_approval()
                if approval:
                    valid, reason, ctx = self.validate_approval(approval)
                    if valid:
                        self.execute_approval(approval, ctx)
                    elif reason not in {"already_seen"}:
                        aid = approval.get("id")
                        with self.lock:
                            already_reported = self.state.get("last_rejected_approval_id") == aid and self.state.get("last_rejected_reason") == reason
                        if not already_reported:
                            with self.lock:
                                self.state["last_rejected_approval_id"] = aid
                                self.state["last_rejected_reason"] = reason
                                self.state["last_approval_result"] = {
                                    "approval_id": aid,
                                    "processed_at_utc": iso_now(),
                                    "status": "REJECTED_BY_EXECUTOR",
                                    "reason": reason,
                                }
                            self._save_state()
                            self._event("approval_rejected", approval_id=aid, reason=reason)
                            self.publish_status()
            except Exception as exc:
                self._event("approval_loop_error", error=f"{type(exc).__name__}:{exc}")
            self.stop_event.wait(self.poll_seconds)

    def startup_audit(self):
        # Verifies private API authentication without publishing balances.
        balances = self.client.balances()
        nonzero = [r for r in balances if Decimal(str(r.get("available", "0"))) + Decimal(str(r.get("inOrder", "0"))) > 0]
        self._event("private_api_authenticated", nonzero_asset_count=len(nonzero), dry_run=self.dry_run)

        # Existing open orders are inventoried but NOT canceled during installation.
        try:
            open_orders = self.client.open_orders()
        except BitvavoError as exc:
            self._event("startup_open_orders_failed", error=str(exc))
            open_orders = []
        unknown_existing = []
        with self.lock:
            known = set(self.state.get("authorized_client_order_ids", []))
        for order in open_orders if isinstance(open_orders, list) else []:
            if order.get("clientOrderId") not in known:
                unknown_existing.append({
                    "market": order.get("market"),
                    "orderId": order.get("orderId"),
                    "clientOrderId": order.get("clientOrderId"),
                    "operatorId": order.get("operatorId"),
                    "side": order.get("side"),
                    "orderType": order.get("orderType"),
                    "status": order.get("status"),
                })
        self._event("startup_order_inventory", open_order_count=len(open_orders) if isinstance(open_orders, list) else 0,
                    unknown_existing_count=len(unknown_existing))
        # Important: existing manual orders do not trigger an automatic freeze at first install.
        self.publish_status()

    def run(self):
        self.startup_audit()
        ws_thread = threading.Thread(target=self.websocket_loop, name="bitvavo-account-ws", daemon=True)
        ws_thread.start()
        try:
            self.approval_loop()
        except KeyboardInterrupt:
            pass
        finally:
            self.stop_event.set()
            self.publish_status()


if __name__ == "__main__":
    Executor().run()
