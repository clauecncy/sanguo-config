import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from catalog_trust import evidence_status


class TrustTests(unittest.TestCase):
    def test_direct_image(self):
        self.assertEqual(evidence_status('游戏内截图','自身缴械2回合'),'可信')

    def test_web_even_with_full_text(self):
        self.assertEqual(evidence_status('第三方结构化资料','完整正文'),'需要确认')

    def test_missing_or_incomplete(self):
        for text in (None,'','受智力影'):
            self.assertEqual(evidence_status('游戏内截图',text),'需要确认')
        self.assertEqual(evidence_status('游戏内截图','摘要',True),'需要确认')

    def test_missing_provenance(self):
        self.assertEqual(evidence_status(None,'历史标了已核'),'需要确认')
