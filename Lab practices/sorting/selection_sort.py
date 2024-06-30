def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        smallest = i
        for j in range(i+1, n):
            if A[j] < A[smallest]:
                smallest = j
        if smallest != i:
            A[smallest], A[i] = A[i], A[smallest]
    return A


if __name__ == "__main__":
    A = [100, 8, 9, 7, 6, 4, 6, 8, 4, 231, 884, 54]
    selection_sort(A)
