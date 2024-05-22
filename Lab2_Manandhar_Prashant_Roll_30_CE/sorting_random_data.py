import random
import time
import matplotlib.pyplot as plt
from sorting_algorithm import merge_sort, quick_sort, selection_sort, insertion_sort
from copy import deepcopy
import sys

# Increase recursion limit to avoid recursion errors for large datasets
sys.setrecursionlimit(20000)


def create_worst_case_merge_sort_array(arr):
    """Create the worst-case array for merge sort.

    This function constructs an array that will result in the worst-case time complexity
    for the merge sort algorithm. 

    Args:
        arr (list): The input array.

    Returns:
        list: The worst-case array for merge sort.
    """
    if len(arr) <= 1:
        return arr  # Base case for recursion

    mid = len(arr) // 2
    left = create_worst_case_merge_sort_array(arr[:mid])
    right = create_worst_case_merge_sort_array(arr[mid:])

    # Merge the two halves in a specific order to create the worst case for merge sort
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if i < len(left):
            result.append(left[i])
            i += 1
        if j < len(right):
            result.append(right[j])
            j += 1

    # Ensure that all elements from left and right are added
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def create_best_case_quick_sort_array(arr, start, end):
    """Create the best-case array for quick sort.

    This function constructs an array that will result in the best-case time complexity
    for the quick sort algorithm. 

    Args:
        arr (list): The input array.
        start (int): The start index of the array.
        end (int): The end index of the array.

    Returns:
        list: The best-case array for quick sort.
    """
    # Sort the array to generate best-case scenario
    arr = sorted(arr)

    if start > end:
        return []

    mid = (start + end) // 2
    left = create_best_case_quick_sort_array(arr, start, mid - 1)
    right = create_best_case_quick_sort_array(arr, mid + 1, end)

    # Place the middle element at the end to simulate it being the pivot
    return left + right + [arr[mid]]


def generate_random_array(size):
    """Generate a random array of given size.

    This function generates a random array of integers within a specified range.

    Args:
        size (int): The size of the array to generate.

    Returns:
        list: The generated random array.
    """
    return [random.randint(-10000, 10000) for _ in range(size)]


def generate_graph():
    """Generate a graph comparing sorting algorithms.

    This function compares the performance of various sorting algorithms by plotting
    their execution times for different array sizes. It evaluates the performance of
    Merge Sort, Quick Sort, Insertion Sort, and Selection Sort under different scenarios
    such as general case, best case, and worst case.
    """
    # Generate breakpoints for array sizes
    breakpoints = [i*100 for i in range(1, 21)]
    random_numbers = generate_random_array(breakpoints[-1])

    # Generate arrays of different sizes for testing
    random_numbers_list = [random_numbers[0:i] for i in breakpoints]
    sorted_array = [sorted(data_set)
                    for data_set in deepcopy(random_numbers_list)]

    worst_case_quick_sort_list = deepcopy(sorted_array)
    best_case_merge_sort_list = deepcopy(sorted_array)

    best_case_quick_sort_list = [create_best_case_quick_sort_array(
        data_set, 0, len(data_set) - 1) for data_set in deepcopy(random_numbers_list)]
    worst_case_merge_sort_list = [create_worst_case_merge_sort_array(
        data_set) for data_set in deepcopy(random_numbers_list)]

    # Initialize lists to store time taken for each sorting algorithm
    time_taken_merge_sort = []
    time_taken_merge_sort_best_case = []
    time_taken_merge_sort_worst_case = []
    time_taken_quick_sort = []
    time_taken_quick_sort_best_case = []
    time_taken_quick_sort_worst_case = []
    time_taken_insertion_sort = []
    time_taken_selection_sort = []

    # Measure time taken for each sorting algorithm
    for data_set in deepcopy(random_numbers_list):
        # Time taken for Merge Sort (General Case)
        start_time = time.perf_counter()
        merge_sort(data_set, 0, len(data_set) - 1)
        merge_sort_endtime = time.perf_counter() - start_time
        time_taken_merge_sort.append(merge_sort_endtime)

    for data_set in deepcopy(best_case_merge_sort_list):
        # Time taken for Merge Sort (Best Case)
        start_time = time.perf_counter()
        merge_sort(data_set, 0, len(data_set) - 1)
        merge_sort_best_endtime = time.perf_counter() - start_time
        time_taken_merge_sort_best_case.append(merge_sort_best_endtime)

    for data_set in deepcopy(worst_case_merge_sort_list):
        # Time taken for Merge Sort (Worst Case)
        start_time = time.perf_counter()
        merge_sort(data_set, 0, len(data_set) - 1)
        merge_sort_worst_endtime = time.perf_counter() - start_time
        time_taken_merge_sort_worst_case.append(merge_sort_worst_endtime)

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Quick Sort (General Case)
        start_time = time.perf_counter()
        quick_sort(data_set, 0, len(data_set) - 1)
        quick_sort_endtime = time.perf_counter() - start_time
        time_taken_quick_sort.append(quick_sort_endtime)

    for data_set in deepcopy(best_case_quick_sort_list):
        # Time taken for Quick Sort (best Case)
        start_time = time.perf_counter()
        quick_sort(data_set, 0, len(data_set) - 1)
        quick_sort_best_endtime = (time.perf_counter() - start_time)
        time_taken_quick_sort_best_case.append(quick_sort_best_endtime)

    for data_set in deepcopy(worst_case_quick_sort_list):
        # Time taken for Quick Sort (Worst Case)
        start_time = time.perf_counter()
        quick_sort(data_set, 0, len(data_set) - 1)
        quick_sort_worst_endtime = (time.perf_counter() - start_time)
        time_taken_quick_sort_worst_case.append(quick_sort_worst_endtime)

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Insertion Sort (General Case)
        start_time = time.perf_counter()
        insertion_sort(data_set)
        insertion_sort_endtime = time.perf_counter() - start_time
        time_taken_insertion_sort.append(insertion_sort_endtime)

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Selection Sort (General Case)
        start_time = time.perf_counter()
        selection_sort(data_set.copy())  # Use a copy to preserve original data
        selection_sort_endtime = time.perf_counter()-start_time
        time_taken_selection_sort.append(selection_sort_endtime)

    # Plotting
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
    plt.title('Comparison of Merge and Quick Sort (General, Best, Worst) ')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

    ax1.plot(breakpoints, time_taken_merge_sort, label='Merge Sort')
    ax1.plot(breakpoints, time_taken_quick_sort, label='Quick Sort')
    ax1.set_xlabel('Array Size')
    ax1.set_ylabel('Time Taken (seconds)')
    ax1.set_title('Comparison of Merge Sort and Quick Sort')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(breakpoints, time_taken_merge_sort_best_case,
             label='Merge Sort (Best Case)')
    ax2.plot(breakpoints, time_taken_quick_sort_best_case,
             label='Quick Sort (Best Case)')
    ax2.set_xlabel('Array Size')
    ax2.set_ylabel('Time Taken (seconds)')
    ax2.set_title('Comparison of Best Case of Merge Sort and Quick Sort')
    ax2.legend()
    ax2.grid(True)

    ax3.plot(breakpoints, time_taken_merge_sort_worst_case,
             label='Merge Sort (Worst Case)')
    ax3.plot(breakpoints, time_taken_quick_sort_worst_case,
             label='Quick Sort (Worst Case)')
    ax3.set_xlabel('Array Size')
    ax3.set_ylabel('Time Taken (seconds)')
    ax3.set_title('Comparison of Worst Case of Merge Sort and Quick Sort')
    ax3.legend()
    ax3.grid(True)

    ax4.plot(breakpoints, time_taken_insertion_sort, label='Insertion Sort')
    ax4.plot(breakpoints, time_taken_selection_sort, label='Selection Sort')
    ax4.set_xlabel('Array Size')
    ax4.set_ylabel('Time Taken (seconds)')
    ax4.set_title('Comparison of Insertion Sort and Selection Sort')
    ax4.legend()
    ax4.grid(True)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Display the plots
    plt.show()


if __name__ == "__main__":
    generate_graph()
