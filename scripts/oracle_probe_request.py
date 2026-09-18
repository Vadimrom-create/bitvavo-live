#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUEST = ROOT / "oracle_probe_request.json"
OUTPUT = ROOT / "oracle_requested_probe.json"
BASE = "http://144.24.206.128:8787"
MARKET_RE = re.compile(r"^[A-Z0-9]{2,20}-EUR$")


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def get_json(path: str, params: dict[str, object] | None = None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "bitvavo-live-oracle-request/1.0"})
    with urllib.request.urlopen(req, timeout=7) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    req = json.loads(REQUEST.read_text(encoding="utf-8"))
    market = str(req.get("market", "")).upper()
    stake_eur = float(req.get("stake_eur", 75))
    if not MARKET_RE.fullmatch(market):
        raise SystemExit("invalid market")
    payload = get_json("/quote", {"market": market, "stake_eur": stake_eur})
    out = {
        "schema": "oracle_requested_probe_v1",
        "requested_at_utc": now_iso(),
        "market": market,
        "stake_eur": stake_eur,
        "probe": payload,
    }
    OUTPUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"requested Oracle probe: {market} ok={payload.get('ok')}")


if __name__ == "__main__":
    main()
