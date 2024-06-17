import random
import time
import matplotlib.pyplot as plt
from sorting_algorithm import merge_sort, quick_sort
from copy import deepcopy

import sys
sys.setrecursionlimit(20000)  # Adjust the number as needed


def generate_random_array(size):
    """Generate a random array of given size."""
    return [random.randint(0, 1000) for _ in range(size)]


def generate_graph():
    """Generate a graph comparing sorting algorithms."""
    breakpoints = [i*100 for i in range(1, 21)]
    random_numbers = generate_random_array(breakpoints[-1])

    random_numbers_list = [random_numbers[0:i] for i in breakpoints]

    # Generate data for best and worst cases of Merge Sort and Quick Sort
    sorted_data = [sorted(data_set)
                   for data_set in deepcopy(random_numbers_list)]
    reverse_sorted_data = [sorted(data_set, reverse=True)
                           for data_set in deepcopy(random_numbers_list)]

    # Initialize lists to store time taken for each sorting algorithm
    time_taken_merge_sort = []
    time_taken_merge_sort_best_case = []
    time_taken_merge_sort_worst_case = []
    time_taken_quick_sort = []
    time_taken_quick_sort_best_case = []
    time_taken_quick_sort_worst_case = []

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Merge Sort (General Case)
        start_time = time.perf_counter()
        merge_sort(data_set, 0, len(data_set) - 1)
        merge_sort_endtime = time.perf_counter() - start_time
        time_taken_merge_sort.append(merge_sort_endtime)

    for data_set in deepcopy(sorted_data):
        # Time taken for Merge Sort (Best Case)
        start_time = time.perf_counter()
        merge_sort(data_set, 0, len(data_set) - 1)
        merge_sort_best_endtime = (time.perf_counter() - start_time)
        time_taken_merge_sort_best_case.append(merge_sort_best_endtime)

    for data_set in deepcopy(reverse_sorted_data):
        # Time taken for Merge Sort (Worst Case)
        start_time = time.perf_counter()
        merge_sort(data_set, 0, len(data_set) - 1)
        merge_sort_worst_endtime = time.perf_counter() - start_time
        time_taken_merge_sort_worst_case.append(
            merge_sort_worst_endtime)

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Quick Sort (General Case)
        start_time = time.perf_counter()
        quick_sort(data_set, 0, len(data_set) - 1)
        quick_sort_endtime = time.perf_counter() - start_time
        time_taken_quick_sort.append(quick_sort_endtime)

    for data_set in deepcopy(sorted_data):
        # Time taken for Quick Sort (Best Case)
        start_time = time.perf_counter()
        quick_sort(data_set, 0, len(data_set) - 1)
        quick_sort_best_endtime = (time.perf_counter() - start_time)
        time_taken_quick_sort_best_case.append(quick_sort_best_endtime)

    for data_set in deepcopy(reverse_sorted_data):
        # Time taken for Quick Sort (Worst Case)
        start_time = time.perf_counter()
        quick_sort(data_set, 0, len(data_set) - 1)
        quick_sort_worst_endtime = time.perf_counter() - start_time
        time_taken_quick_sort_worst_case.append(
            quick_sort_worst_endtime)

    plt.plot(breakpoints, time_taken_merge_sort, label='Merge Sort')
    plt.plot(breakpoints, time_taken_merge_sort_best_case,
             label='Merge Sort (Best Case)')
    plt.plot(breakpoints, time_taken_merge_sort_worst_case,
             label='Merge Sort (Worst Case)')
    plt.plot(breakpoints, time_taken_quick_sort, label='Quick Sort')
    plt.plot(breakpoints, time_taken_quick_sort_best_case,
             label='Quick Sort (Best Case)')
    plt.plot(breakpoints, time_taken_quick_sort_worst_case,
             label='Quick Sort (Worst Case)')

    plt.xlabel('Array Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Comparison of Merge Sort and Quick Sort')
    plt.legend()
    plt.grid(True)
    # plt.yscale('log')
    plt.show()


generate_graph()
