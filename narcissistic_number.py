import unittest

"""
A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of
the number of digits in a given base. In this Kata, we will restrict ourselves to decimal
(base 10).

For example, take 153 (3 digits):
 ==> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

and 1634 (4 digits):
 ==> 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
"""


def is_narcissistic(number):
    """Must return True if number is narcissistic"""
    return sum([pow(int(x), len(str(number))) for x in str(number)]) == number


class TestNarcissistic(unittest.TestCase):
    def test_narcissistic_7(self):
        self.assertEqual(is_narcissistic(7), True)

    def test_narcissistic_153(self):
        self.assertEqual(is_narcissistic(153), True)

    def test_narcissistic_1634(self):
        self.assertEqual(is_narcissistic(1634), True)

    def test_narcissistic_122(self):
        self.assertEqual(is_narcissistic(122), False)

    def test_narcissistic_4887(self):
        self.assertEqual(is_narcissistic(4887), False)

    def test_narcissistic_19283(self):
        self.assertEqual(is_narcissistic(19283), False)


if __name__ == "__main__":
    unittest.main()
