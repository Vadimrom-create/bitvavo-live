from __future__ import annotations

import json
import os
from pathlib import Path
import tempfile
import unittest

from research.trend_cache_guard import ensure_fresh_trend_cache


def daily_raw(last_ts):
    rows=[]
    start=last_ts-94*86_400_000
    for i in range(95):
        t=start+i*86_400_000
        p=100+i*0.1
        rows.append([t,str(p),str(p+1),str(p-1),str(p+0.2),str(1000+i)])
    return list(reversed(rows))  # Bitvavo returns latest -> earliest


class FakeClient:
    def __init__(self):
        self.calls=[]
    def get(self,path,params=None):
        self.calls.append((path,params))
        return daily_raw(1_800_000_000_000)


class TrendCacheGuardTests(unittest.TestCase):
    def test_refreshes_stale_profile_even_when_global_cache_timestamp_is_fresh(self):
        with tempfile.TemporaryDirectory() as d:
            old=os.getcwd()
            try:
                os.chdir(d)
                Path("v4_trend_cache.json").write_text(json.dumps({
                    "version":4,
                    "updated_ts":1000,
                    "markets":{"BTC-EUR":{"updated_ts":10,"last":50}}
                }),encoding="utf-8")
                client=FakeClient()
                audit=ensure_fresh_trend_cache(client,["BTC-EUR"],1000,max_age_sec=100)
                cache=json.loads(Path("v4_trend_cache.json").read_text())
            finally:
                os.chdir(old)
        self.assertEqual(audit["stale_before_count"],1)
        self.assertEqual(audit["refreshed_count"],1)
        self.assertEqual(cache["markets"]["BTC-EUR"]["updated_ts"],1000)
        self.assertEqual(len(client.calls),1)

    def test_does_not_refetch_fresh_profile(self):
        with tempfile.TemporaryDirectory() as d:
            old=os.getcwd()
            try:
                os.chdir(d)
                Path("v4_trend_cache.json").write_text(json.dumps({
                    "version":4,
                    "updated_ts":1000,
                    "markets":{"BTC-EUR":{"updated_ts":950,"last":50}}
                }),encoding="utf-8")
                client=FakeClient()
                audit=ensure_fresh_trend_cache(client,["BTC-EUR"],1000,max_age_sec=100)
            finally:
                os.chdir(old)
        self.assertEqual(audit["stale_before_count"],0)
        self.assertEqual(len(client.calls),0)


if __name__=="__main__":
    unittest.main()
