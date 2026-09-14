import unittest
from unittest.mock import patch


class CollectionBudgetTests(unittest.TestCase):
    def test_expired_optional_request_does_not_touch_network_or_consume_rate_slot(self):
        from research.http import PublicClient
        c=PublicClient()
        with patch('research.http.time.monotonic',return_value=100),patch('urllib.request.urlopen') as network:
            with self.assertRaisesRegex(RuntimeError,'DEADLINE'): c.capture('/AAA-EUR/candles',deadline=99)
            network.assert_not_called()
            self.assertEqual(c.next_request,0)

    def test_unenriched_markets_remain_in_population_after_budget_expires(self):
        from pipeline import collect_universe
        from research.http import PublicClient
        markets=[{'market':m} for m in ('AAA-EUR','BBB-EUR')]
        with patch('pipeline.time.monotonic',return_value=100),patch('urllib.request.urlopen') as network:
            result=collect_universe(PublicClient(),markets,{},0,budget_seconds=0,priority=['BBB-EUR'])
        self.assertEqual(set(result),{'AAA-EUR','BBB-EUR'})
        self.assertTrue(all(r['errors'] for r in result.values()))
        network.assert_not_called()
