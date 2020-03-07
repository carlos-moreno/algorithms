import unittest
from sum_list import sum_list


class TestSomaElementos(unittest.TestCase):
    def test_result_is_10(self):
        self.assertEqual(sum_list([2, 3, 5]), 10)

    def test_result_is_20(self):
        self.assertEqual(sum_list([2, 3, 5, 6, 4]), 20)

    def test_result_is_5(self):
        self.assertEqual(sum_list([1, 2, 2]), 5)
