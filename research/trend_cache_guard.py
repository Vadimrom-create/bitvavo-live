"""Per-market freshness guard for the V4 daily trend cache.

The frozen V4 cache uses a global TTL. A single newly-added/missing market can
refresh that global timestamp while leaving existing market profiles stale.
This operational guard refreshes stale profiles individually before V4 runs,
without changing any V4 scoring formula or threshold.
"""
from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from research.common import finite
from v4_common import TREND_CACHE, daily_profile_from_candles, load_trend_cache, save_json

AUDIT_PATH = Path("trend_cache_guard.json")
MAX_PROFILE_AGE_SEC = 2 * 3600


def _parse(raw):
    rows=[]
    for item in raw or []:
        if not isinstance(item,(list,tuple)) or len(item)<6:
            continue
        try:
            rows.append({
                "t": int(item[0]),
                "o": float(item[1]),
                "h": float(item[2]),
                "l": float(item[3]),
                "c": float(item[4]),
                "v": float(item[5]),
            })
        except (TypeError,ValueError):
            continue
    rows.sort(key=lambda x:x["t"])
    return rows


def ensure_fresh_trend_cache(client, markets, now_ts, max_age_sec=MAX_PROFILE_AGE_SEC):
    cache=load_trend_cache()
    profiles=cache.setdefault("markets",{})
    names=list(dict.fromkeys(m for m in markets if isinstance(m,str) and m.endswith("-EUR")))
    stale=[]
    for market in names:
        age=now_ts-finite((profiles.get(market) or {}).get("updated_ts"),0)
        if market not in profiles or age>max_age_sec:
            stale.append(market)

    refreshed=[]
    errors={}
    def one(market):
        try:
            raw=client.get(f"/{market}/candles",{"interval":"1d","limit":95})
            profile=daily_profile_from_candles(_parse(raw))
            if not profile:
                raise RuntimeError("INSUFFICIENT_DAILY_PROFILE")
            profile["updated_ts"]=now_ts
            profile.pop("last_error",None)
            return market,profile,None
        except Exception as exc:
            return market,None,f"{type(exc).__name__}:{exc}"

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures=[pool.submit(one,m) for m in stale]
        for fut in as_completed(futures):
            market,profile,error=fut.result()
            if profile:
                profiles[market]=profile
                refreshed.append(market)
            else:
                errors[market]=error

    # This timestamp describes the guard execution only. Per-market updated_ts
    # remains the source of truth for freshness.
    cache["updated_ts"]=now_ts
    from datetime import datetime,timezone
    cache["updated_at_utc"]=datetime.fromtimestamp(now_ts,timezone.utc).isoformat()
    save_json(TREND_CACHE,cache)

    fresh=sum(
        1 for m in names
        if now_ts-finite((profiles.get(m) or {}).get("updated_ts"),0)<=max_age_sec
    )
    audit={
        "schema":"trend_cache_guard_v1",
        "checked_market_count":len(names),
        "stale_before_count":len(stale),
        "refreshed_count":len(refreshed),
        "refresh_error_count":len(errors),
        "fresh_after_count":fresh,
        "max_profile_age_sec":max_age_sec,
        "errors":errors,
    }
    AUDIT_PATH.write_text(json.dumps(audit,ensure_ascii=False,separators=(",",":")),encoding="utf-8")
    return audit
