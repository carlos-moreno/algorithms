import unittest
from hypotenuse import is_hypotenuse, sum_hypotenuse

class TestHypotenuse(unittest.TestCase):
    def test_resul_5_is_true(self):
        self.assertEqual(is_hypotenuse(5), True)

    def test_resul_6_is_false(self):
        self.assertEqual(is_hypotenuse(6), False)

    def test_resul_10_is_true(self):
        self.assertEqual(is_hypotenuse(10), True)

    def test_resul_11_is_false(self):
        self.assertEqual(is_hypotenuse(11), False)

class TestSumHypotenuse(unittest.TestCase):
    def test_result_9_is_5(self):
        self.assertEqual(sum_hypotenuse(9), 5)

    def test_result_10_is_15(self):
        self.assertEqual(sum_hypotenuse(10), 15)

    def test_result_25_is_105(self):
        self.assertEqual(sum_hypotenuse(25), 105)