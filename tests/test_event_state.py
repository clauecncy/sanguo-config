import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from event_state import projections


class EventProjectionTests(unittest.TestCase):
    def setUp(self):
        self.state = {
            'user_id': 'test',
            'event_id': 's2-2026-09-30',
            'warehouse': {'support': {'status': 'confirmed'}},
            'lineup': {'teams': []},
            'stage': 'partial',
            'locked': None,
        }

    def test_existing_projection_keeps_default_boundary(self):
        report = projections('event', self.state)['event/当前状态.md'].decode('utf-8')
        self.assertIn('清风支援来源推定与装备截图确认分开。', report)

    def test_new_event_uses_its_own_boundary_without_changing_state(self):
        self.state['evidence_boundary'] = 'Only visible equipment is confirmed.'
        before = copy.deepcopy(self.state)
        report = projections('event', self.state)['event/当前状态.md'].decode('utf-8')
        self.assertIn(self.state['evidence_boundary'], report)
        self.assertNotIn('清风支援来源推定', report)
        self.assertEqual(self.state, before)


if __name__ == '__main__':
    unittest.main()
