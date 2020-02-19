import unittest
from algorithms import mult_two, best_stock, radix


class TestMultTwo(unittest.TestCase):
    def test_mult_trhee_two_is_six(self):
        self.assertEqual(mult_two(3, 2), 6)

    def test_mult_one_zero_is_zero(self):
        self.assertEqual(mult_two(1, 0), 0)

    def test_mult_five_one_is_five(self):
        self.assertEqual(mult_two(5, 1), 5)


class TestBestStock(unittest.TestCase):
    def test_result_is_atx(self):
        self.assertEqual(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}), "ATX")

    def test_result_is_tasi(self):
        self.assertEqual(best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}), "TASI")

    def test_result_is_cbds(self):
        self.assertEqual(
            best_stock({"FKS": 203.43, "TGAV": 1002.45, "CBDS": 1002.46}), "CBDS"
        )


class TestRadix(unittest.TestCase):
    def test_result_is_175(self):
        self.assertEqual(radix("AF", 16), 175)

    def test_result_is_5(self):
        self.assertEqual(radix("101", 2), 5)

    def test_result_is_26(self):
        self.assertEqual(radix("101", 5), 26)

    def test_result_is_1_negative(self):
        self.assertEqual(radix("AB", 10), -1)
        self.assertEqual(radix("909", 9), -1)
