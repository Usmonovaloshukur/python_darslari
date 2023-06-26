import unittest
from max import maxabc

class Max(unittest.TestCase):
    def test_maxabc(self):
        self.assertEqual(maxabc(25,15,65), 65)
        self.assertEqual(maxabc(25,15,-65), 25)
        self.assertEqual(maxabc(1,2,3), 3)
        self.assertEqual(maxabc(12.25,12.2601,12.26013), 12.26013)


