import unittest
from sequential_search import sequential_search
from string_matching import string_matching


class TextAlgorithmStrategies(unittest.TestCase):
    A = [89, 74, 97, 37, 86, 84, 53, 46, 78, 56, 80, 54, 41, 65, 54,
         94, 94, 27, 76, 75, 74, 80, 93, 63, 16, 44, 35, 19, 2, 83]

    def sequential_test_1(self):
        self.assertEqual(sequential_search(self.A, 89), 1)

    def test_element_present(self):
        self.assertEqual(sequential_search(self.A, 89), 0)
        self.assertEqual(sequential_search(self.A, 97), 2)
        self.assertEqual(sequential_search(self.A, 41), 12)
        self.assertEqual(sequential_search(self.A, 83), 29)

    def test_element_not_present(self):
        self.assertEqual(sequential_search(self.A, 100), -1)
        self.assertEqual(sequential_search(self.A, -1), -1)

    def test_multiple_occurrences(self):
        self.assertEqual(sequential_search(self.A, 94), 15)
        self.assertEqual(sequential_search(self.A, 74), 1)
        self.assertEqual(sequential_search(self.A, 80), 10)

    def test_empty_array(self):
        empty_array = []
        self.assertEqual(sequential_search(empty_array, 89), -1)

    def test_single_element_array(self):
        single_element_array = [89]
        self.assertEqual(sequential_search(single_element_array, 89), 0)
        self.assertEqual(sequential_search(single_element_array, 100), -1)

    def test_first_and_last_elements(self):
        self.assertEqual(sequential_search(self.A, 89), 0)
        self.assertEqual(sequential_search(self.A, 83), 29)

    def test_substring_present(self):
        self.assertEqual(string_matching("Prashant", "ras"), 1)
        self.assertEqual(string_matching("hello world", "world"), 6)
        self.assertEqual(string_matching("abcdef", "cde"), 2)
        self.assertEqual(string_matching("testcase", "case"), 4)

    def test_substring_not_present(self):
        self.assertEqual(string_matching("Prashant", "xyz"), -1)
        self.assertEqual(string_matching("hello world", "planet"), -1)
        self.assertEqual(string_matching("abcdef", "gh"), -1)

    def test_substring_at_edges(self):
        self.assertEqual(string_matching("Prashant", "Pra"), 0)
        self.assertEqual(string_matching("Prashant", "ant"), 5)

    def test_empty_substring(self):
        self.assertEqual(string_matching("Prashant", ""), 0)
        self.assertEqual(string_matching("", ""), 0)

    def test_empty_string(self):
        self.assertEqual(string_matching("", "ras"), -1)
        self.assertEqual(string_matching("", "a"), -1)


if __name__ == "__main__":
    unittest.main()
