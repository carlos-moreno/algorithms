import unittest
from max_element import max_element


class TestMaxElement(unittest.TestCase):
    def test_result_is_7(self):
        self.assertEqual(max_element([1, 7, 4, 0]), 7)

    def test_result_is_50(self):
        self.assertEqual(max_element([34, 21, -9, 5, 50]), 50)

    def test_result_is_3_negativo(self):
        self.assertEqual(max_element([-4, -3, -10, -1020, -50]), -3)
