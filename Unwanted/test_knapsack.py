import unittest
from Knapsack import knapsack_01_brute_force, knapsack_fractional_brute_force, knapsack_fractional_greedy, knapsack_01_dynamic


# class TestKnapsackBruteForce(unittest.TestCase):

#     def test_case_1(self):
#         values = [60, 100, 120]
#         weights = [10, 20, 30]
#         capacity = 50
#         expected_result = 220
#         self.assertEqual(knapsack_01_brute_force(
#             weights,values, capacity), expected_result)

#     def test_case_2(self):
#         values = [10, 20, 30]
#         weights = [1, 1, 1]
#         capacity = 2
#         expected_result = 50
#         self.assertEqual(knapsack_01_brute_force(
#             weights,values, capacity), expected_result)

#     def test_case_3(self):
#         values = [1, 4, 5, 7]
#         weights = [1, 3, 4, 5]
#         capacity = 7
#         expected_result = 9
#         self.assertEqual(knapsack_01_brute_force(
#             weights,values, capacity), expected_result)

#     def test_case_4(self):
#         values = [15, 10, 9, 5]
#         weights = [1, 5, 3, 4]
#         capacity = 8
#         expected_result = 29
#         self.assertEqual(knapsack_01_brute_force(
#             weights,values, capacity), expected_result)

#     def test_case_5(self):
#         values = []
#         weights = []
#         capacity = 10
#         expected_result = 0
#         self.assertEqual(knapsack_01_brute_force(
#             weights,values, capacity), expected_result)

#     def test_case_6(self):
#         values = [10, 40, 30, 50]
#         weights = [5, 4, 6, 3]
#         capacity = 10
#         expected_result = 90
#         self.assertEqual(knapsack_01_brute_force(
#             weights,values, capacity), expected_result)


# if __name__ == '__main__':
#     unittest.main()


class TestKnapsackFractional(unittest.TestCase):
    def test_knapsack_fractional(self):
        # Test case 1: General case with different weights and profits
        weights = [2, 2, 3]
        profits = [6, 10, 12]
        capacity = 6
        result = knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, [0.5, 1, 1])

        # Test case 2: No items to select
        weights = []
        profits = []
        capacity = 5
        result = knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, [])

        # Test case 3: Capacity is zero
        weights = [2, 3, 4]
        profits = [3, 4, 5]
        capacity = 0
        result = knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, [])

        # Test case 4: Single item that fits
        weights = [3]
        profits = [10]
        capacity = 5
        result = knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, [1.0])

        # Test case 5: Single item that doesn't fit
        weights = [7]
        profits = [10]
        capacity = 5
        result = knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, [])

        # Test case 6: Multiple items, all fit exactly
        weights = [1, 2, 3]
        profits = [6, 10, 12]
        capacity = 6
        result = knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, [1.0, 1.0, 1.0])

        # Test case 7: Choosing the most profitable items within capacity
        weights = [1, 3, 4, 5]
        profits = [1, 4, 5, 7]
        capacity = 7
        result = knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, [0, 1, 1, 0])

        # Test case 8: Items with same weight but different profits
        weights = [2, 2, 2]
        profits = [10, 20, 30]
        capacity = 5
        result = knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, [0.5, 1.0, 1.0])

        # Test case 9: Edge case where all items can be included
        weights = [1, 2, 3]
        profits = [10, 20, 30]
        capacity = 6
        result = knapsack_fractional_greedy(weights, profits, capacity)
        self.assertEqual(result, [1.0, 1.0, 1.0])


if __name__ == "_main_":
    unittest.main()
