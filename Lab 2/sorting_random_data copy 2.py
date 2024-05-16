import random
import time
import matplotlib.pyplot as plt
from sorting_algorithm import merge_sort, quick_sort
from copy import deepcopy


def generate_random_array(size):
    """Generate a random array of given size."""
    return [random.randint(0, 1000) for _ in range(size)]


def measure_time(func, data):
    """Measure the time taken by a sorting function."""
    start_time = time.perf_counter()
    func(data, 0, len(data) - 1)
    return time.perf_counter() - start_time


def generate_graph():
    """Generate a graph comparing sorting algorithms."""
    breakpoints = [i * 100 for i in range(1, 21)]
    random_numbers = generate_random_array(breakpoints[-1])

    random_numbers_list = [random_numbers[:i] for i in breakpoints]

    time_taken_merge_sort = []
    time_taken_quick_sort = []

    runs_per_size = 10

    for data_set in random_numbers_list:
        merge_sort_times = []
        quick_sort_times = []

        for _ in range(runs_per_size):
            merge_sort_data = deepcopy(data_set)
            quick_sort_data = deepcopy(data_set)

            merge_sort_times.append(measure_time(merge_sort, merge_sort_data))
            quick_sort_times.append(measure_time(quick_sort, quick_sort_data))

        time_taken_merge_sort.append(sum(merge_sort_times) / runs_per_size)
        time_taken_quick_sort.append(sum(quick_sort_times) / runs_per_size)

    plt.plot(breakpoints, time_taken_merge_sort, label='Merge Sort')
    plt.plot(breakpoints, time_taken_quick_sort, label='Quick Sort')

    plt.xlabel('Array Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Comparison of Merge Sort and Quick Sort')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Use logarithmic scale for better visualization
    plt.show()


generate_graph()
