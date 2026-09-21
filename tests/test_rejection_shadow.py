import unittest
from pathlib import Path
class RejectionShadowContractTests(unittest.TestCase):
    def test_shadow_script_is_non_actionable(self):
        text=Path("scripts/update_rejection_shadow.py").read_text()
        self.assertIn('"affects_buy_gate":False',text)
        self.assertIn('"affects_email":False',text)
        self.assertIn("STRUCTURAL_RANGE_TOO_NARROW",text)
        self.assertIn("first_later_qualifying_entry",text)
if __name__=="__main__": unittest.main()
