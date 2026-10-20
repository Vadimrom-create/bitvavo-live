import gzip
import json
import math
import tempfile
import unittest
from pathlib import Path

from scripts.research_dl_price_paths import (
    bounds, frozen_confirmed, inspect_one, report_for_archive, select_due,
)

STAMP=1_800_000_000.0

class StubClient:
    def __init__(self,broken=False):
        self.calls=[]
        self.broken=broken
    def get(self,url,params,cache=False):
        self.calls.append((url,params))
        t=params["start"]
        if self.broken:
            return []
        return [[x,1.0,1.1,0.92,1.04,10] for x in range(t,params["end"],300000)]

def event(t=STAMP,name="FET-EUR",price=1.0):
    return {"scan_ts":t,"scan_id":"scan-1","scan_at_utc":"2027-01-15T08:00:00+00:00",
            "market":name,"scan_price_eur":price,"baseline_v4_available":True}

class PilotTests(unittest.TestCase):
    def test_future_horizons_excluded(self):
        out=select_due([event()],STAMP+24*3600+301)
        self.assertEqual([x["hours"] for x in out],[24])
        self.assertEqual(select_due([event()],STAMP+24*3600),[])

    def test_strict_5m_complete_reference_only(self):
        item={**event(),"hours":24}
        client=StubClient()
        one=inspect_one(item,client,STAMP+25*3600)
        self.assertEqual(one["status"],"COMPLETE")
        self.assertGreater(one["mfe_pct"],5)
        self.assertLess(one["mae_pct"],0)
        self.assertIsNone(one["executable_net_pnl_eur"])
        self.assertFalse(one["future_book_depth_verified"])
        self.assertEqual(client.calls[0][1]["interval"],"5m")

    def test_no_trade_gap_is_incomplete_not_zero(self):
        item={**event(),"hours":24}
        one=inspect_one(item,StubClient(broken=True),STAMP+25*3600)
        self.assertEqual(one["status"],"INCOMPLETE")
        self.assertIsNone(one["mfe_pct"])
        self.assertIsNone(one["close_pct"])

    def test_invalid_horizon_fails_before_api(self):
        client=StubClient()
        result=inspect_one({**event(),"hours":72},client,STAMP+25*3600)
        self.assertEqual(result["status"],"SOURCE_ERROR")
        self.assertEqual(len(client.calls),0)

    def test_selection_dedup_earliest_scan_market(self):
        with tempfile.TemporaryDirectory() as d:
            files=[]
            for idx,t in enumerate((STAMP,STAMP+1000)):
                path=Path(d)/("scan"+str(idx)+".json.gz")
                doc={"scan_id":str(idx),"scan_at_utc":__import__("datetime").datetime.fromtimestamp(t,__import__("datetime").timezone.utc).isoformat(),
                     "observations":[
                         {"market":"FET-EUR","price_eur":1.0,"acceleration":{"state":"CONFIRMED_ACCELERATION"}},
                         {"market":"VTHO-EUR","price_eur":2.0,"acceleration":{"state":"BUILDING_ACCELERATION"}}]}
                with gzip.open(path,"wt") as f:
                    json.dump(doc,f)
                files.append(str(path))
            entries,bad=frozen_confirmed(files)
            self.assertEqual(bad,{})
            self.assertEqual(len(entries),1)
            self.assertEqual(entries[0]["scan_id"],"0")

    def test_no_cherry_picking_and_no_pnl(self):
        rows=[event(STAMP+i*300,name=f"T{i}-EUR") for i in range(3)]
        # Events at STAMP; no market outcome based selection.
        import unittest.mock as mock
        doc={"scan_id":"x","scan_at_utc":__import__("datetime").datetime.fromtimestamp(STAMP,__import__("datetime").timezone.utc).isoformat(),
             "observations":[{"market":e["market"],"price_eur":1,"acceleration":{"state":"CONFIRMED_ACCELERATION"}} for e in rows]}
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"one.json.gz"
            with gzip.open(path,"wt") as f:json.dump(doc,f)
            z=report_for_archive([str(path)],StubClient(),STAMP+25*3600,max_per_horizon=2)
            self.assertEqual(z["horizons"]["24"]["eligible_sample"],2)
            self.assertEqual(z["horizons"]["48"]["eligible_sample"],0)
            self.assertFalse(z["executable_pnl_comparable"])
            self.assertIsNone(z["net_pnl_eur"])

    def test_bounds_never_cross_future(self):
        with self.assertRaises(ValueError):
            bounds(STAMP,48,STAMP+24*3600)
        req,n=bounds(STAMP,24,STAMP+25*3600)
        self.assertLessEqual(req["end"],int((STAMP+25*3600)*1000))
        self.assertLessEqual(n,288)

if __name__=="__main__":
    unittest.main()
