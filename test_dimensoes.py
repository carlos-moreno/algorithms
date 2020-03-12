import unittest
from dimensoes import dimensoes


class DimensoesTestCase(unittest.TestCase):
    def test_result_is_3x1(self):
        self.assertEqual(dimensoes([[1], [2], [3]]), "3X1")

    def test_result_is_2x3(self):
        self.assertEqual(dimensoes([[1, 2, 3], [4, 5, 6]]), "2X3")
