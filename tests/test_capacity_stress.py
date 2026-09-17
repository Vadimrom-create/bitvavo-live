import unittest
import json
from research.capacity_stress import simulate


class CapacityStressTests(unittest.TestCase):
    def test_nominal_and_degraded_real_transport_budget(self):
        for name,kwargs in [('nominal',{}),('errors5',{'error_percent':5}),('errors10',{'error_percent':10}),
                            ('timeouts10',{'error_percent':10,'timeouts':True}),('two_consumers',{'consumers':2})]:
            with self.subTest(name=name):
                r=simulate(**kwargs)
                print('CAPACITY_STRESS '+json.dumps({'scenario':name,**r}),flush=True)
                self.assertLessEqual(r['peak_60s_points'],750,r)
                self.assertLessEqual(r['duration_seconds'],300.001,r)
                self.assertEqual(r['responses_older_than_300s_at_end'],0,r)
                if name in ('nominal','errors5','errors10'):
                    self.assertEqual(r['markets_both_timeframes_completed'],430,r)
                    self.assertEqual(r['freshness_abandoned_calls'],0,r)
                if name=='timeouts10':self.assertGreater(r['freshness_abandoned_calls'],0,r)
