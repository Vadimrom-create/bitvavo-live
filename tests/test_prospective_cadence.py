import unittest
from research.common import utc
from research.prospective_cadence import begin, finish, health, slot_at


class CadenceTests(unittest.TestCase):
    def test_holes_detected_and_not_relabelled_as_backfilled(self):
        now=slot_at(20000)+400; prior=now-4*1800
        state,attempt,status=begin({},now,'a',prior)
        self.assertEqual(status['status'],'MISSED')
        self.assertEqual(len(state['missed_slots']),3)
        state,receipt,status=finish(state,attempt,now+60,{'v3':{'checked_at_utc':utc(now),'status':'OK'}})
        self.assertEqual(status['status'],'OK');self.assertEqual(status['missed_slots_count'],3)
        self.assertEqual(receipt['recovery'],'LATE_CURRENT_CAPTURE_NO_BACKFILL')
        self.assertFalse(status['historical_holes_backfilled'])
    def test_completed_window_not_collected_twice(self):
        now=slot_at(20000)+50;s,a,_=begin({},now,'a')
        s,_,_=finish(s,a,now+10,{'v3':{'checked_at_utc':utc(now),'status':'OK'}})
        _,b,_=begin(s,now+20,'b');self.assertFalse(b['run'])
        _,c,_=begin(s,now+1800,'c');self.assertTrue(c['run'])
    def test_failures_have_bounded_retries_and_old_outputs_never_complete(self):
        now=slot_at(20000)+10;s,a,_=begin({},now,'a')
        s,r,_=finish(s,a,now+20,{'v3':{'checked_at_utc':utc(now-100),'status':'OK'}})
        self.assertFalse(r['collection_complete'])
        _,b,_=begin(s,now+30,'b');self.assertEqual(b['reason'],'RETRY_COOLDOWN')
        s,b,_=begin(s,now+601,'b');self.assertTrue(b['run'])
        _,c,_=begin(s,now+1202,'c');self.assertEqual(c['reason'],'RETRY_LIMIT')
    def test_delayed_is_distinct_from_missed_and_age_is_visible(self):
        t=slot_at(20000)
        self.assertEqual(health({},t+1)['status'],'DELAYED')
        self.assertEqual(health({},t+301)['status'],'MISSED')
