import random
import time
import matplotlib.pyplot as plt
from sorting import insertion_sort, selection_sort
from copy import deepcopy


def generate_random_array(size):
    """Generate a random array of given size."""
    return [random.randint(-1000, 1000) for _ in range(size)]


def generate_graph():
    """Generate a graph comparing sorting algorithms."""
    breakpoints = [i*100 for i in range(1, 21)]  # Adjusted for clarity
    random_numbers = generate_random_array(breakpoints[-1])
    
    random_numbers_list = [random_numbers[0:i] for i in breakpoints]

    # Generate data for best and worst cases of Insertion Sort
    sorted_data = [sorted(data_set)
                   for data_set in deepcopy(random_numbers_list)]
    reverse_sorted_data = [sorted(data_set, reverse=True)
                           for data_set in deepcopy(random_numbers_list)]

    # Initialize lists to store time taken for each sorting algorithm
    time_taken_insertion_sort = []
    time_taken_insertion_sort_best_case = []
    time_taken_insertion_sort_worst_case = []
    time_taken_selection_sort = []

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Insertion Sort (General Case)
        start_time = time.time()
        insertion_sort(data_set)
        insertion_sort_endtime = time.time() - start_time
        time_taken_insertion_sort.append(insertion_sort_endtime)

    for data_set in deepcopy(random_numbers_list):
        # Time taken for Selection Sort
        start_time = time.time()
        selection_sort(data_set.copy())  # Use a copy to preserve original data
        selection_sort_endtime = time.time()-start_time
        time_taken_selection_sort.append(selection_sort_endtime)

    for data_set in sorted_data:
        # Time taken for Insertion Sort (Best Case)
        start_time = time.time()
        insertion_sort(data_set)
        insertion_sort_best_endtime = time.time() - start_time
        time_taken_insertion_sort_best_case.append(insertion_sort_best_endtime)

    for data_set in reverse_sorted_data:
        # Time taken for Insertion Sort (Worst Case)
        start_time = time.time()
        insertion_sort(data_set)
        insertion_sort_worst_endtime = time.time() - start_time
        time_taken_insertion_sort_worst_case.append(
            insertion_sort_worst_endtime)

    print(f"Time Taken by Insertion Sort:\t {insertion_sort_endtime}\n")
    print(f"Time Taken by Selection Sort:\t{selection_sort_endtime}\n")
    print(
        f"Time Taken by Insertion Sort (Best Case):\t {insertion_sort_best_endtime}\n")
    print(
        f"Time Taken by Insertion Sort (Worst Case):\t{insertion_sort_worst_endtime}\n")

    print("----------------------------------------------\n")

    print("Time Interval After Each Inverval by Insertion Sort (General Case):\n",
          time_taken_insertion_sort, "\n")
    print("Time Interval After Each Inverval by Insertion Sort (Best Case):\n",
          time_taken_insertion_sort_best_case, "\n")
    print("Time Interval After Each Inverval by Insertion Sort (Worst Case):\n",
          time_taken_insertion_sort_worst_case, "\n")
    print("Time Interval After Each Inverval by Selection Sort:\n",
          time_taken_selection_sort, "\n")

 # Plotting the graph
    plt.plot(breakpoints, time_taken_insertion_sort, label='Insertion Sort')
    plt.plot(breakpoints, time_taken_insertion_sort_best_case,
             label='Insertion Sort (Best Case)')
    plt.plot(breakpoints, time_taken_insertion_sort_worst_case,
             label='Insertion Sort (Worst Case)')
    plt.plot(breakpoints, time_taken_selection_sort, label='Selection Sort')

    plt.xlabel('Array Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title(
        'Comparison of Insertion Sort (General, Best, Worst) and Selection Sort')
    plt.legend()
    plt.grid(True)
    plt.show()


generate_graph()


# import random
# import time
# from sorting import insertion_sort, selection_sort
# import matplotlib.pyplot as plt
# from copy import deepcopy


# def generate_random_array(size):
#     random_array = [random.randint(-1000, 1000) for _ in range(size)]
#     return random_array


# def generate_graph():
#     breakpoints = [i*100 for i in range(20)]
#     random_numbers = generate_random_array(breakpoints[-1])
#     random_numbers_list = []
#     for i in breakpoints:
#         random_numbers_list.append(random_numbers[0:i])
#     start_time = time.time()
#     time_taken_insertion_sort = []
#     time_taken_insertion_sort_best_case = []
#     time_taken_insertion_sort_worst_case = []
#     time_taken_selection_sort = []

#     # Create a copy of random_numbers_list
#     copied_list = deepcopy(random_numbers_list)

#     for j in copied_list:
#         insertion_sort(j)
#         insertion_sort_endtime = time.time() - start_time
#         time_taken_insertion_sort.append(insertion_sort_endtime)

#     print(f"Time Taken by Insertion Sort: {insertion_sort_endtime}")

#     # Create a copy of random_numbers_list
#     copied_list = deepcopy(random_numbers_list)

#     start_time = time.time()
#     for j in copied_list:
#         selection_sort(j)
#         selection_sort_endtime = time.time()-start_time
#         time_taken_selection_sort.append(selection_sort_endtime)

#     print(f"Time Taken by Selection Sort:{selection_sort_endtime} ")

#     """
#     for best case of the insertion sort, we have sort the random array
#     """
#     # Create a copy of random_numbers_list
#     copied_list = deepcopy(random_numbers_list)
#     sorted_random_numbers_list = []
#     for random_numbers in copied_list:
#         random_numbers.sort()
#         sorted_random_numbers_list.append(random_numbers)

#     start_time = time.time()
#     for j in sorted_random_numbers_list:
#         insertion_sort(j)
#         insertion_sort_best_endtime = time.time() - start_time
#         time_taken_insertion_sort_best_case.append(insertion_sort_best_endtime)

#     print(
#         f"Time Taken by Insertion Sort (Base Case): {insertion_sort_best_endtime}")

#     """
#     for worst case of the insertion sort, we have sort the random array in reverse manner
#     """
#     # Create a copy of random_numbers_list
#     copied_list = deepcopy(random_numbers_list)
#     reverse_sorted_random_numbers_list = []
#     for random_numbers in copied_list:
#         random_numbers.sort(reverse=True)
#         reverse_sorted_random_numbers_list.append(random_numbers)

#     start_time = time.time()
#     for j in reverse_sorted_random_numbers_list:
#         insertion_sort(j)
#         insertion_sort_worst_endtime = time.time() - start_time
#         time_taken_insertion_sort_worst_case.append(
#             insertion_sort_worst_endtime)

#     print(
#         f"Time Taken by Insertion Sort (Base Case): {insertion_sort_best_endtime}")

#     # Plotting the graph
#     plt.plot(breakpoints, time_taken_insertion_sort, label='Insertion Sort')
#     plt.plot(breakpoints, time_taken_insertion_sort_best_case,
#              label='Insertion Sort (Best Case)')
#     plt.plot(breakpoints, time_taken_insertion_sort_worst_case,
#              label='Insertion Sort (Worst Case)')
#     plt.plot(breakpoints, time_taken_selection_sort, label='Selection Sort')

#     plt.xlabel('Array Size')
#     plt.ylabel('Time Taken (seconds)')
#     plt.title(
#         'Comparison of Insertion Sort (General, Best, Worst) and Selection Sort')
#     plt.legend()
#     plt.grid(True)
#     plt.show()


# generate_graph()
