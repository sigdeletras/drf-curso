""" 
Sample test
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the cal module"""

    def test_add_numer(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numer(self):
        """Test adding numbers together."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
