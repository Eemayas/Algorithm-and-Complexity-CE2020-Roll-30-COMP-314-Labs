import random
import time
import matplotlib.pyplot as plt
from sorting_algorithm import merge_sort, quick_sort, selection_sort, insertion_sort
from copy import deepcopy
import sys
sys.setrecursionlimit(20000)


def create_best_case_quick_sort(arr, start, end):
    arr = sorted(arr)
    # Base case: If start is greater than end, return an empty list
    if start > end:
        return []
    # Find the middle index of the current range
    mid = (start + end) // 2
    # Recursively construct the left subarray
    left = create_best_case_quick_sort(arr, start, mid - 1)
    # Recursively construct the right subarray
    right = create_best_case_quick_sort(arr, mid + 1, end)
    # Place the middle element at the end to simulate it being the pivot
    return left + right + [arr[mid]]


def generate_random_array(size):
    """Generate a random array of given size."""
    return [random.randint(-10000, 10000) for _ in range(size)]


def generate_graph():
    """Generate a graph comparing sorting algorithms."""
    breakpoints = [i*100 for i in range(1, 21)]
    random_numbers = generate_random_array(breakpoints[-1])

    random_numbers_list = [random_numbers[0:i] for i in breakpoints]

    # Initialize lists to store time taken for each sorting algorithm
    time_taken_merge_sort = []
    time_taken_quick_sort = []
    time_taken_quick_sort_best_case = []
    time_taken_insertion_sort = []
    time_taken_selection_sort = []

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Merge Sort (General Case)
        start_time = time.perf_counter()
        merge_sort(data_set, 0, len(data_set) - 1)
        merge_sort_endtime = time.perf_counter() - start_time
        time_taken_merge_sort.append(merge_sort_endtime)

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Quick Sort (General Case)
        start_time = time.perf_counter()
        quick_sort(data_set, 0, len(data_set) - 1)
        quick_sort_endtime = time.perf_counter() - start_time
        time_taken_quick_sort.append(quick_sort_endtime)

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Insertion Sort (General Case)
        start_time = time.perf_counter()
        insertion_sort(data_set)
        insertion_sort_endtime = time.perf_counter() - start_time
        time_taken_insertion_sort.append(insertion_sort_endtime)

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Selection Sort
        start_time = time.perf_counter()
        selection_sort(data_set.copy())  # Use a copy to preserve original data
        selection_sort_endtime = time.perf_counter()-start_time
        time_taken_selection_sort.append(selection_sort_endtime)

    fig, ((ax1, ax2)) = plt.subplots(1, 2, figsize=(15, 8))

    ax1.plot(breakpoints, time_taken_merge_sort, label='Merge Sort')
    ax1.plot(breakpoints, time_taken_quick_sort, label='Quick Sort')

    ax1.set_xlabel('Array Size')
    ax1.set_ylabel('Time Taken (seconds)')
    ax1.set_title('Comparison of Merge and Quick Sort')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(breakpoints, time_taken_insertion_sort, label='Insertion Sort')
    ax2.plot(breakpoints, time_taken_selection_sort, label='Selection Sort')

    ax2.set_xlabel('Array Size')
    ax2.set_ylabel('Time Taken (seconds)')
    ax2.set_title('Comparison of Insertion and Selection Sort')
    ax2.legend()
    ax2.grid(True)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Display the plots
    plt.show()


generate_graph()
