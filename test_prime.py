import unittest
from primo import is_prime, qtd_number_primes


class TestPrimo(unittest.TestCase):
    def test_result_2_is_true(self):
        self.assertEqual(is_prime(2), True)

    def test_result_3_is_true(self):
        self.assertEqual(is_prime(3), True)

    def test_result_4_is_false(self):
        self.assertEqual(is_prime(4), False)

    def test_result_5_is_true(self):
        self.assertEqual(is_prime(5), True)

    def test_result_810_is_false(self):
        self.assertEqual(is_prime(810), False)

    def test_result_811_is_true(self):
        self.assertEqual(is_prime(811), True)


class TestQtdNumberPrime(unittest.TestCase):
    def test_result_2_is_1(self):
        self.assertEqual(qtd_number_primes(2), 1)

    def test_result_3_is_2(self):
        self.assertEqual(qtd_number_primes(3), 2)

    def test_result_4_is_2(self):
        self.assertEqual(qtd_number_primes(4), 2)

    def test_result_5_is_3(self):
        self.assertEqual(qtd_number_primes(5), 3)

    def test_result_121_is_30(self):
        self.assertEqual(qtd_number_primes(121), 30)
