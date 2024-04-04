import unittest
from sorting import insertion_sort, selection_sort


class TestSort(unittest.TestCase):
    """
    A class containing test cases for insertion sort and selection sort algorithms.
    """

    # Test data for insertion sort and selection sort
    data_negative = {"input": [-2, 45, 0, 11, -9, 88, -97, -202, 747],
                     "output": [-202, -97, -9, -2, 0, 11, 45, 88, 747]}

    data_positive = {"input": [12, 11, 13, 5, 6],
                     "output": [5, 6, 11, 12, 13]}

    data_descending = {"input": [9, 8, 7, 6, 5, 4, 3, 2, 1],
                       "output": [1, 2, 3, 4, 5, 6, 7, 8, 9]}

    data_ascending = {"input": [1, 2, 3, 4, 5, 6, 7, 8, 9],
                      "output": [1, 2, 3, 4, 5, 6, 7, 8, 9]}

    data_duplicates = {"input": [4, 2, 2, 3, 4, 1, 1, 5, 5, 6, 7, 3, 7, 8, 8, 9, 6, 9],
                       "output": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]}

    data_single = {"input": [45],
                   "output": [45]}

    data_empty = {"input": [],
                  "output": []}

    def test_sort(self):
        """Test the sorting function."""
        input_data = [12, 11, 13, 5, 6]
        result = insertion_sort(self.data_positive["input"])
        self.assertEqual(result, self.data_positive["output"])
        self.assertNotEqual(insertion_sort([]), [12])

    def test_sort_insertion_negative(self):
        """Test insertion sort with negative numbers."""
        self.assertEqual(insertion_sort(
            self.data_negative["input"]), self.data_negative["output"])
        self.assertEqual(selection_sort(
            self.data_negative["input"]), self.data_negative["output"])

    def test_sort_insertion_positive(self):
        """Test insertion sort with positive numbers."""
        self.assertEqual(insertion_sort(
            self.data_positive["input"]), self.data_positive["output"])
        self.assertEqual(selection_sort(
            self.data_positive["input"]), self.data_positive["output"])

    def test_sort_insertion_descending(self):
        """Test insertion sort with descending numbers."""
        self.assertEqual(insertion_sort(
            self.data_descending["input"]), self.data_descending["output"])
        self.assertEqual(selection_sort(
            self.data_descending["input"]), self.data_descending["output"])

    def test_sort_insertion_ascending(self):
        """Test insertion sort with ascending numbers."""
        self.assertEqual(insertion_sort(
            self.data_ascending["input"]), self.data_ascending["output"])
        self.assertEqual(selection_sort(
            self.data_ascending["input"]), self.data_ascending["output"])

    def test_sort_insertion_duplicate(self):
        """Test insertion sort with duplicate numbers."""
        self.assertEqual(insertion_sort(
            self.data_duplicates["input"]), self.data_duplicates["output"])
        self.assertEqual(selection_sort(
            self.data_duplicates["input"]), self.data_duplicates["output"])

    def test_sort_insertion_empty_list(self):
        """Test sorting an empty list."""
        self.assertEqual(insertion_sort(
            self.data_empty["input"]), self.data_empty["output"])
        self.assertEqual(selection_sort(
            self.data_empty["input"]), self.data_empty["output"])

    def test_sort_insertion_single_element_list(self):
        """Test sorting a list with a single element."""
        self.assertEqual(insertion_sort(
            self.data_single["input"]), self.data_single["output"])
        self.assertEqual(selection_sort(
            self.data_single["input"]), self.data_single["output"])


if __name__ == "__main__":
    unittest.main()
