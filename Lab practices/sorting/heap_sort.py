import math


def heapify(A, i, length):
    left = 2*i+1
    right = 2*i+2
    if left < length and A[i] < A[left]:
        largest_index = left
    else:
        largest_index = i
    if right < length and A[largest_index] < A[right]:
        largest_index = right
    if largest_index != i:
        A[i], A[largest_index] = A[largest_index], A[i]
        heapify(A, largest_index, length)
    return A


def build_max_heap(A):
    for i in range(len(A)//2, -1, -1):
        heapify(A, i, len(A))


def heap_sort(A):
    build_max_heap(A)
    for i in range(len(A)-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, 0, i)
    return A


if __name__ == "__main__":
    # Sample list to be heapified
    sample_list = [4, 10, 3, 5, 1]

    print("Original list:")
    print(sample_list)

    # Heapifying the list
    heap_sort(sample_list)

    print("Heapified list:")
    print(sample_list)
