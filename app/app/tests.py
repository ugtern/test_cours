from django.test import TestCase
from app.calc import calc_multiple, calc_sum, calc_subtract


class CalcTests(TestCase):

    def test_multiple_function(self):
        self.assertEqual(calc_multiple(2, 2), 4)

    def test_sum_function(self):
        self.assertEqual(calc_sum(8, 10), 18)

    def test_subtract_function(self):
        self.assertEqual(calc_subtract(6, 2), 4)
