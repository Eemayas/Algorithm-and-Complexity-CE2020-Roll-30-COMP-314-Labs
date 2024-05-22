from copy import deepcopy
import random
from sorting_random_data import create_worst_case_merge_sort_array, create_best_case_quick_sort_array

# Example usage:
# random_array = [random.randint(0, 100) for _ in range(10)]
random_array = [94, 67, 15, 45, 27, 95, 89, 40, 54, 42]
# random_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print("Original Array:", random_array)

print("Worst Case Array for Quick Sort:", sorted(
    random_array))

worst_case_array = create_worst_case_merge_sort_array(
    sorted(deepcopy(random_array), key=lambda x: random.random()))
worst_case_array = create_worst_case_merge_sort_array(
    deepcopy(random_array))

print("Worst Case Array for Merge Sort:", worst_case_array)

print("Best Case Array for Quick Sort:", create_best_case_quick_sort_array(
    random_array, 0, len(random_array)-1))

print("Best Case Array for Merge Sort:", sorted(
    random_array))
