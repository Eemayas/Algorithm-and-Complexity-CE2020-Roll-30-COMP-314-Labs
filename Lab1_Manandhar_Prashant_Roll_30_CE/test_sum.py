import unittest
from sum import sum


class TestSum(unittest.TestCase):
    """
    A class containing test cases for the sum function.
    """

    def test_sum_positive_numbers(self):
        """
        Test summing positive numbers.
        """
        input_data = [3, 4, 5]
        result = sum(input_data)
        self.assertEqual(result, 12)

    def test_sum_empty_list(self):
        """
        Test summing an empty list.
        """
        self.assertEqual(sum([]), 0)

    def test_sum_negative_numbers(self):
        """
        Test summing negative numbers.
        """
        input_data = [-3, -4, -5]
        result = sum(input_data)
        self.assertEqual(result, -12)

    def test_sum_mixed_numbers(self):
        """
        Test summing a mix of positive and negative numbers.
        """
        input_data = [3, -4, 5, -2, 1]
        result = sum(input_data)
        self.assertEqual(result, 3)

    def test_sum_single_element_list(self):
        """
        Test summing a list with a single element.
        """
        self.assertEqual(sum([10]), 10)

    def test_sum_large_numbers(self):
        """
        Test summing large numbers.
        """
        input_data = [1000000, 2000000, 3000000]
        result = sum(input_data)
        self.assertEqual(result, 6000000)

    def test_sum_float_numbers(self):
        """
        Test summing floating-point numbers.
        """
        input_data = [1.5, 2.5, 3.5]
        result = sum(input_data)
        self.assertEqual(result, 7.5)


if __name__ == "__main__":
    unittest.main()
