import copy,io,tempfile,unittest,urllib.error
from pathlib import Path
from unittest.mock import Mock,patch
from research.common import utc,atomic_json
from scripts.solaire_v3_shadow import source_error,fetch_external_price_snapshot

class SourceGapTests(unittest.TestCase):
    def test_http_errors_are_classified_not_assumed_permanent(self):
        for code,kind in [(403,'ACCESS_OR_REGIONAL_POLICY'),(451,'ACCESS_OR_REGIONAL_POLICY'),(429,'RATE_LIMITED'),
                          (404,'ENDPOINT_NOT_FOUND'),(500,'TRANSIENT_EXTERNAL'),(401,'AUTHENTICATION_OR_SOURCE_POLICY')]:
            err=urllib.error.HTTPError('https://example.org/path?secret=hidden',code,'reason',{},io.BytesIO())
            r=source_error('test',err);self.assertEqual(r['http_status'],code);self.assertEqual(r['classification'],kind)
            self.assertFalse(r['permanent_unusability_proven']);self.assertNotIn('secret',r['endpoint'])
    def test_all_external_sources_may_fail_without_requiring_them_for_core(self):
        with patch('scripts.solaire_v3_shadow._json_url',side_effect=TimeoutError):
            prices,errors=fetch_external_price_snapshot({'BTC'})
        self.assertEqual(prices,{})
        self.assertTrue(errors);self.assertTrue(all(e['mandatory_for_bitvavo_core'] is False for e in errors))
