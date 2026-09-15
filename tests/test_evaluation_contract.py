import unittest
from research.history import connect, ingest
from research.evaluation import market_control


def bars(gap=0):
    values=[dict(t=i*300000,o=100,h=101,l=100,c=100,v=1) for i in range(12)]
    values.append(dict(t=3600000+gap,o=100,h=107,l=100,c=106,v=1))
    return values


class EvaluationContractTests(unittest.TestCase):
    def test_gap_until_crossing_never_confirms_short_event(self):
        db=connect();cs=bars(13800000)
        ingest(db,dict(scan_id='s',scan_ts=18000,policy='V4',observations=[],candles_5m={'AAA-EUR':cs}))
        r=market_control(db,[dict(market='AAA-EUR',price_eur=106,change_24h_pct=6)],18000)[0]
        self.assertIsNone(r['event_onset_ts'])
        self.assertEqual(r['event_observability'],'INSUFFICIENT_CONTINUITY')

    def test_continuity_duplicates_order_and_partial_last_bar(self):
        from research.evaluation import short_event
        cs=bars()
        self.assertEqual(short_event(list(reversed(cs)),3900)['onset_ts'],0)
        self.assertEqual(short_event(cs,3899)['onset_ts'],None)
        self.assertEqual(short_event(cs+[cs[-1]],3900)['onset_ts'],0)
        r=short_event(cs+[{**cs[-1],'h':108}],3900)
        self.assertEqual(r['status'],'CONFLICTING_CANDLE')
        self.assertIsNone(r['onset_ts'])

    def test_historical_detection_survives_absence_from_current_top(self):
        from research.evaluation import market_control_current
        db=connect()
        old={'market':'ZZZ-EUR','price_eur':100,'baseline':{'action_status':'WATCH'},'decision':'SURVEILLE'}
        ingest(db,dict(scan_id='old',scan_ts=100,policy='V4',observations=[old]))
        observations=[dict(market=str(i)+'-EUR',price_eur=1,change_24h_pct=i) for i in range(70)]
        observations += [dict(market='ZZZ-EUR',price_eur=100,change_24h_pct=-1)]
        current=market_control_current(observations,{'watch':[]},{'watch':[]})
        self.assertEqual(current[-1]['presence'],'ABSENT_FROM_CURRENT_PUBLISHED_LISTS')
        history=market_control(db,observations,1000)
        row=next(r for r in history if r['market']=='ZZZ-EUR')
        self.assertEqual(row['first_detected_ever_ts'],100)
        self.assertEqual(len(history),71)
