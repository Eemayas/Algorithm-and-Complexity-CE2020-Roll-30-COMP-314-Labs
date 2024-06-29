import math


def partition(A, p, r):
    pivot = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] < pivot:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)
    return A


if __name__ == "__main__":
    A = [100, 8, 9, 7, 6, 4, 6, 8, 4, 231, 884, 54]
    quick_sort(A, 0, len(A)-1)
    print(A)
