# Quick Sort Algorithm Implementation
def quick_sort(A, p, r):
    """
    Sorts the array A using the Quick Sort algorithm.

    Parameters:
    A (list): The input list to be sorted.
    p (int): The starting index of the list segment to be sorted.
    r (int): The ending index of the list segment to be sorted.
    """
    if p < r:
        # Partition the array and get the pivot index
        q = partition(A, p, r)
        # Recursively apply quick sort to the left of the pivot
        quick_sort(A, p, q - 1)
        # Recursively apply quick sort to the right of the pivot
        quick_sort(A, q + 1, r)
    return A

# Merge Sort Algorithm Implementation
def merge_sort(A, p, r):
    """
    Sorts the array A using the Merge Sort algorithm.

    Parameters:
    A (list): The input list to be sorted.
    p (int): The starting index of the list segment to be sorted.
    r (int): The ending index of the list segment to be sorted.
    """
    if p < r:
        # Find the middle point to divide the array into two halves
        q = (p + r) // 2
        # Recursively apply merge sort to the first half
        merge_sort(A, p, q)
        # Recursively apply merge sort to the second half
        merge_sort(A, q + 1, r)
        # Merge the two halves
        merge(A, p, q, r)
    return A

# Merge Fuction Implementation
def merge(A, p, q, r):
    """
    Merges two halves of the array A.

    Parameters:
    A (list): The input list with segments to be merged.
    p (int): The starting index of the first half.
    q (int): The ending index of the first half.
    r (int): The ending index of the second half.
    """
    n1 = q - p + 1
    n2 = r - q

    # Create temporary arrays
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Copy data to temporary arrays L and R
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]

    # Add sentinel values to the end of temporary arrays
    L[n1] = float('inf')
    R[n2] = float('inf')

    i = j = 0

    # Merge the temporary arrays back into A
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

# Partition Function Implementation
def partition(array, low, high):
    """
    Partitions the array around the pivot element.

    Parameters:
    array (list): The input list to be partitioned.
    low (int): The starting index for the partitioning process.
    high (int): The ending index for the partitioning process.

    Returns:
    int: The index of the pivot element after partitioning.
    """
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# Insertion Sort Algorithm Implementation
def insertion_sort(arr):
    """
    Sorts the array using the Insertion Sort algorithm.

    Parameters:
    arr (list): The input list to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Selection Sort Algorithm Implementation
def selection_sort(array):
    """
    Sorts the array using the Selection Sort algorithm.

    Parameters:
    array (list): The input list to be sorted.

    Returns:
    list: The sorted list.
    """
    n = len(array)
    for i in range(n):
        key = i
        for j in range(i + 1, n):
            if array[j] < array[key]:
                key = j
        array[i], array[key] = array[key], array[i]
    return array
