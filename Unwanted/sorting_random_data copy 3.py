import random
import time
import matplotlib.pyplot as plt
from sorting_algorithm import merge_sort, quick_sort, selection_sort, insertion_sort
from copy import deepcopy
import sys
sys.setrecursionlimit(20000)


def generate_random_array(size):
    """Generate a random array of given size."""
    return [random.randint(-10000, 10000) for _ in range(size)]


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
    time_taken_insertion_sort = []
    time_taken_insertion_sort_best_case = []
    time_taken_insertion_sort_worst_case = []
    time_taken_selection_sort = []

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

    for data_set in sorted_data:
        # Time taken for Insertion Sort (Best Case)
        start_time = time.perf_counter()
        insertion_sort(data_set)
        insertion_sort_best_endtime = (time.perf_counter() - start_time)
        time_taken_insertion_sort_best_case.append(insertion_sort_best_endtime)

    for data_set in reverse_sorted_data:
        # Time taken for Insertion Sort (Worst Case)
        start_time = time.perf_counter()
        insertion_sort(data_set)
        insertion_sort_worst_endtime = time.perf_counter() - start_time
        time_taken_insertion_sort_worst_case.append(
            insertion_sort_worst_endtime)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

    ax1.plot(breakpoints, time_taken_merge_sort, label='Merge Sort')
    ax1.plot(breakpoints, time_taken_quick_sort, label='Quick Sort')
    ax1.plot(breakpoints, time_taken_insertion_sort, label='Insertion Sort')
    ax1.plot(breakpoints, time_taken_selection_sort, label='Selection Sort')

    ax1.set_xlabel('Array Size')
    ax1.set_ylabel('Time Taken (seconds)')
    ax1.set_title('Comparison of Merge, Insertion, Selection and Quick Sort')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(breakpoints, time_taken_merge_sort_best_case,
             label='Merge Sort (Best Case)')
    ax2.plot(breakpoints, time_taken_quick_sort_best_case,
             label='Quick Sort (Best Case)')
    ax2.plot(breakpoints, time_taken_insertion_sort_best_case,
             label='Insertion Sort (Best Case)')

    ax2.set_xlabel('Array Size')
    ax2.set_ylabel('Time Taken (seconds)')
    ax2.set_title(
        'Comparison of Best Case of Merge, Insertion and Quick Sort')
    ax2.legend()
    ax2.grid(True)

    ax3.plot(breakpoints, time_taken_merge_sort_worst_case,
             label='Merge Sort (Worst Case)')
    ax3.plot(breakpoints, time_taken_quick_sort_worst_case,
             label='Quick Sort (Worst Case)')
    ax3.plot(breakpoints, time_taken_insertion_sort_worst_case,
             label='Insertion Sort (Worst Case)')

    ax3.set_xlabel('Array Size')
    ax3.set_ylabel('Time Taken (seconds)')
    ax3.set_title(
        'Comparison of Merge Sort (Worst Case) and Quick Sort (Worst Case)')
    ax3.legend()
    ax3.grid(True)

    # ax4.plot(breakpoints, time_taken_merge_sort, label='Merge Sort')
    # # ax4.plot(breakpoints, time_taken_merge_sort_best_case, label='Merge Sort (Best Case)')
    # # ax4.plot(breakpoints, time_taken_merge_sort_worst_case, label='Merge Sort (Worst Case)')
    # ax4.plot(breakpoints, time_taken_quick_sort, label='Quick Sort')
    # # ax4.plot(breakpoints, time_taken_quick_sort_best_case, label='Quick Sort (Best Case)')
    # # ax4.plot(breakpoints, time_taken_quick_sort_worst_case, label='Quick Sort (Worst Case)')

    # ax4.set_xlabel('Array Size')
    # ax4.set_ylabel('Time Taken (seconds)')
    # ax4.set_title('Comparison of Merge Sort and Quick Sort')
    # ax4.legend()
    # ax4.grid(True)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Display the plots
    plt.show()


generate_graph()
# print(f"Time Taken by Merge Sort:\t {merge_sort_endtime}\n")
# print(
#     f"Time Taken by Merge Sort (Best Case):\t {merge_sort_best_endtime}\n")
# print(
#     f"Time Taken by Merge Sort (Worst Case):\t{merge_sort_worst_endtime}\n")
# print(f"Time Taken by Quick Sort:\t {quick_sort_endtime}\n")
# print(
#     f"Time Taken by Quick Sort (Best Case):\t {quick_sort_best_endtime}\n")
# print(
#     f"Time Taken by Quick Sort (Worst Case):\t{quick_sort_worst_endtime}\n")

# print("----------------------------------------------\n")

# # Define a dictionary to hold the time intervals for different sort cases
# time_intervals = {
# "Merge Sort (General Case)": time_taken_merge_sort,
# "Merge Sort (Best Case)": time_taken_merge_sort_best_case,
# "Merge Sort (Worst Case)": time_taken_merge_sort_worst_case,
# "Quick Sort (General Case)": time_taken_quick_sort,
# "Quick Sort (Best Case)": time_taken_quick_sort_best_case,
# "Quick Sort (Worst Case)": time_taken_quick_sort_worst_case,

# }

# # Find the maximum width of breakpoints
# max_width_breakpoints = max(len(str(b)) for b in breakpoints)

# # Iterate over each sort case and print the time intervals
# for case, intervals in time_intervals.items():
#     print(f"Time Interval After Each Interval by {case}:\n")
#     for i in range(len(breakpoints)):
#         # Adjust spacing for breakpoints and intervals
#         print(
#             f"{breakpoints[i]:<{max_width_breakpoints+15}}\t{intervals[i]}")
#     print("----------------------------------------------\n")

# # Calculate the maximum width required for each column
# max_width_breakpoints = max(len(str(b)) for b in breakpoints)
# max_width_merge_sort = max(len(str(t))
#    for t in time_taken_merge_sort)
# max_width_merge_sort_best_case = max(len(str(t))
#                                      for t in time_taken_merge_sort_best_case)
# max_width_merge_sort_worst_case = max(len(str(t))
#                                       for t in time_taken_merge_sort_worst_case)
# max_width_quick_sort = max(len(str(t))
#    for t in time_taken_quick_sort)
# max_width_quick_sort_best_case = max(len(str(t))
#                                      for t in time_taken_quick_sort_best_case)
# max_width_quick_sort_worst_case = max(len(str(t))
#                                       for t in time_taken_quick_sort_worst_case)

# # Print the table header
# print("Combined Table\n")
# print(f"{'BreakPoints:':<{max_width_breakpoints+15}} {'Merge Sort (General Case):':<{max_width_merge_sort+15}} {'Merge Sort (Best Case):':<{max_width_merge_sort_best_case+15}} {'Merge Sort (Worst Case):':<{max_width_merge_sort_worst_case+15}}{'Quick Sort (General Case):':<{max_width_quick_sort+15}} {'Quick Sort (Best Case):':<{max_width_quick_sort_best_case+15}} {'Quick Sort (Worst Case):':<{max_width_quick_sort_worst_case+15}}")

# # Print the data rows
# for i in range(len(breakpoints)):
#     print(f"{breakpoints[i]:<{max_width_breakpoints}} {time_taken_merge_sort[i]:<{max_width_merge_sort}} {time_taken_merge_sort_best_case[i]:<{max_width_merge_sort_best_case}} {time_taken_merge_sort_worst_case[i]:<{max_width_merge_sort_worst_case}} \
#         {time_taken_quick_sort[i]:<{max_width_quick_sort}} {time_taken_quick_sort_best_case[i]:<{max_width_quick_sort_best_case}} {time_taken_quick_sort_worst_case[i]:<{max_width_quick_sort_worst_case}}")

# plt.xlabel('Array Size')
# plt.ylabel('Time Taken (seconds)')
# plt.title(
#     'Comparison of Merge Sort (General, Best, Worst) and Quick Sort (General, Best, Worst)  ')
# plt.legend()
# plt.grid(True)
# plt.show()

# Plotting the graph
#     plt.plot(breakpoints, time_taken_merge_sort, label='Merge Sort')
#     # plt.plot(breakpoints, time_taken_merge_sort_best_case,
#     #          label='Merge Sort (Best Case)')
#     # plt.plot(breakpoints, time_taken_merge_sort_worst_case,
#     #          label='Merge Sort (Worst Case)')
#     plt.plot(breakpoints, time_taken_quick_sort, label='Quick Sort')
#     # plt.plot(breakpoints, time_taken_quick_sort_best_case,
#     #          label='Quick Sort (Best Case)')
#     # plt.plot(breakpoints, time_taken_quick_sort_worst_case,
#     #          label='Quick Sort (Worst Case)')
