import unittest
from remove_repeat_in_list import remove_duplicates


class TestRemoveRepeatInList(unittest.TestCase):
    def test_result_is_1_2_3(self):
        self.assertEqual(remove_duplicates([1, 2, 1, 1, 3, 3]), [1, 2, 3])

    def test_result_is_1_2_3_4_5_6(self):
        self.assertEqual(remove_duplicates([5, 4, 1, 1, 3, 5, 6, 2]), [1, 2, 3, 4, 5, 6])
