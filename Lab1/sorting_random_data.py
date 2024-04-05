import random
import time
import matplotlib.pyplot as plt # type: ignore
from sorting import insertion_sort, selection_sort
from copy import deepcopy


def generate_random_array(size):
    """Generate a random array of given size."""
    return [random.randint(-1000, 1000) for _ in range(size)]


def generate_graph():
    """Generate a graph comparing sorting algorithms."""
    breakpoints = [i*100 for i in range(1, 21)]
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

    # Define a dictionary to hold the time intervals for different sort cases
    time_intervals = {
        "Insertion Sort (General Case)": time_taken_insertion_sort,
        "Insertion Sort (Best Case)": time_taken_insertion_sort_best_case,
        "Insertion Sort (Worst Case)": time_taken_insertion_sort_worst_case,
        "Selection Sort": time_taken_selection_sort
    }

    # Find the maximum width of breakpoints
    max_width_breakpoints = max(len(str(b)) for b in breakpoints)

    # Iterate over each sort case and print the time intervals
    for case, intervals in time_intervals.items():
        print(f"Time Interval After Each Interval by {case}:\n")
        for i in range(len(breakpoints)):
            # Adjust spacing for breakpoints and intervals
            print(f"{breakpoints[i]:<{max_width_breakpoints+15}}\t{intervals[i]}")
        print("----------------------------------------------\n")

    # Calculate the maximum width required for each column
    max_width_breakpoints = max(len(str(b)) for b in breakpoints)
    max_width_insertion_sort = max(len(str(t))
                                   for t in time_taken_insertion_sort)
    max_width_best_case = max(len(str(t))
                              for t in time_taken_insertion_sort_best_case)
    max_width_worst_case = max(len(str(t))
                               for t in time_taken_insertion_sort_worst_case)
    max_width_selection_sort = max(len(str(t))
                                   for t in time_taken_selection_sort)

    # Print the table header
    print("Combined Table\n")
    print(f"{'BreakPoints:':<{max_width_breakpoints+15}} {'Insertion Sort (General Case):':<{max_width_insertion_sort+15}} {'Insertion Sort (Best Case):':<{max_width_best_case+15}} {'Insertion Sort (Worst Case):':<{max_width_worst_case+15}} {'Selection Sort:':<{max_width_selection_sort+15}}")

    # Print the data rows
    for i in range(len(breakpoints)):
        print(f"{breakpoints[i]:<{max_width_breakpoints+15}} {time_taken_insertion_sort[i]:<{max_width_insertion_sort+15}} {time_taken_insertion_sort_best_case[i]:<{max_width_best_case+15}} {time_taken_insertion_sort_worst_case[i]:<{max_width_worst_case+15}} {time_taken_selection_sort[i]:<{max_width_selection_sort+15}}")
        
        
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
