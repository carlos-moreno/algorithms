import unittest
from algorithms import (
    mult_two,
    best_stock,
    radix,
    second_index,
    first_word,
    first_word_complex,
    bigger_price,
    popular_words,
    between_markers,
    between_markers_complex,
    all_the_same)


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


class TestSecondIndex(unittest.TestCase):
    def test_result_is_3(self):
        self.assertEqual(second_index("sims", "s"), 3)

    def test_result_is_12(self):
        self.assertEqual(second_index("find the river", "e"), 12)

    def test_result_is_none(self):
        self.assertEqual(second_index("hi", " "), None)
        self.assertEqual(second_index("hi mayor", " "), None)

    def test_result_is_5(self):
        self.assertEqual(second_index("hi mr Mayor", " "), 5)


class TestFirstWorld(unittest.TestCase):
    def test_result_is_hello(self):
        self.assertEqual(first_word("Hello world"), "Hello")

    def test_result_is_a(self):
        self.assertEqual(first_word("a word"), "a")

    def test_result_is_hi(self):
        self.assertEqual(first_word("hi"), "hi")


class TestFirstWorldComplex(unittest.TestCase):
    def test_result_is_hello(self):
        self.assertEqual(first_word_complex("Hello world"), "Hello")
        self.assertEqual(first_word_complex("Hello.World"), "Hello")

    def test_result_is_a(self):
        self.assertEqual(first_word_complex(" a word "), "a")

    def test_result_is_hi(self):
        self.assertEqual(first_word_complex("hi"), "hi")

    def test_result_is_dont(self):
        self.assertEqual(first_word_complex("don't touch it"), "don't")

    def test_result_is_greetings(self):
        self.assertEqual(first_word_complex("greetings, friends"), "greetings")

    def test_result_is_and(self):
        self.assertEqual(first_word_complex("... and so on ..."), "and")


class TestBiggerPrice(unittest.TestCase):
    def test_result_is_2_dict(self):
        self.assertEqual(
            bigger_price(
                2,
                [
                    {"name": "bread", "price": 100},
                    {"name": "wine", "price": 138},
                    {"name": "meat", "price": 15},
                    {"name": "water", "price": 1},
                ],
            ),
            [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}],
        )

    def test_result_is_1_dict(self):
        self.assertEqual(
            bigger_price(
                1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
            ),
            [{"name": "whiteboard", "price": 170}],
        )


class TestPopularWords(unittest.TestCase):
    def test_resut_count_is_equal_gives_word(self):
        self.assertEqual(
            popular_words(
                """
            When I was One
            I had just begun
            When I was Two
            I was nearly new
            """,
                ["i", "was", "three", "near"],
            ),
            {"i": 4, "was": 3, "three": 0, "near": 0},
        )


class TestBetweenMarkers(unittest.TestCase):
    def test_result_is_apple(self):
        self.assertEqual(between_markers("What is >apple<", ">", "<"), "apple")
        self.assertEqual(between_markers("What is >apple<", ">", "<"), "apple")

    def test_result_is_car(self):
        self.assertEqual(between_markers("What is $car-", "$", "-"), "car")

    def test_result_is_empty(self):
        self.assertEqual(between_markers("What is ><", ">", "<"), "")


class TestBetweenMarkersComplex(unittest.TestCase):
    def test_result(self):
        self.assertEqual(between_markers_complex("What is >apple<", ">", "<"), "apple")
        self.assertEqual(
            between_markers_complex(
                "<head><title>My new site</title></head>", "<title>", "</title>"
            ),
            "My new site",
        )
        self.assertEqual(between_markers_complex("No[/b] hi", "[b]", "[/b]"), "No")
        self.assertEqual(between_markers_complex("No [b]hi", "[b]", "[/b]"), "hi")
        self.assertEqual(between_markers_complex("No hi", "[b]", "[/b]"), "No hi")
        self.assertEqual(between_markers_complex("No <hi>", ">", "<"), "")


class TestAllTheSame(unittest.TestCase):
    def test_result_is_true(self):
        self.assertEqual(all_the_same([1, 1, 1]), True)
        self.assertEqual(all_the_same(['a', 'a', 'a']), True)
        self.assertEqual(all_the_same([]), True)
        self.assertEqual(all_the_same([1]), True)

    def test_result_is_false(self):
        self.assertEqual(all_the_same([1, 2, 1]), False)
        self.assertEqual(all_the_same([1, 2, 2, 1]), False)
