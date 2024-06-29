def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    return A


if __name__ == "__main__":
    A = [100, 8, 9, 7, 6, 4, 6, 8, 4, 231, 884, 54]
    bubble_sort(A)
    print(A)
