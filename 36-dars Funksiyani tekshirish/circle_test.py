import unittest
from circle import getArea, getUzunlik


class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(10), 314.159)
        self.assertAlmostEqual(getArea(3), 28.27431)

    def test_perimeter(self):
        self.assertAlmostEqual(getUzunlik(10), 62.83138)
        self.assertAlmostEqual(getUzunlik(4), 25.132552)


