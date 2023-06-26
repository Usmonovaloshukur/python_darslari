
import unittest
from tubsonmi import tubsonmi

class TubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubsonmi(7))
        self.assertTrue(tubsonmi(193))
        self.assertTrue(tubsonmi(547))
    def test_false(self):
        self.assertFalse(tubsonmi(6))
        self.assertFalse(tubsonmi(265))
        self.assertFalse(tubsonmi(489))

