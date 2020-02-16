import unittest
from algorithms import mult_two

class TestMultTwo(unittest.TestCase):

    def test_mult_trhee_two_is_six(self):
        self.assertEqual(mult_two(3, 2), 6)

    def test_mult_one_zero_is_zero(self):
        self.assertEqual(mult_two(1, 0), 0)

    def test_mult_five_one_is_five(self):
        self.assertEqual(mult_two(5, 1), 5)
