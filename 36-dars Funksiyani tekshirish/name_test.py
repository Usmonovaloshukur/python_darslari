
import unittest
from asosiy import get_fullname

class NameTest(unittest.TestCase):
    def test_tuliq_ism(self):
        formatted_name = get_fullname('aloshukur', 'usmonov')
        self.assertEqual(formatted_name, "Aloshukur Usmonov")
    def test_tuliq_ism_otasi(self):
        name = get_fullname('aloshukur', 'usmonov', 'islomovich')
        self.assertEqual(name, "Aloshukur Usmonov Islomovich")