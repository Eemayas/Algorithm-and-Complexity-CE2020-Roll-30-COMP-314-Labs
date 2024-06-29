def selection_sort(A):
    n = len(A)
    for i in range(0, n):
        smallest = i
        for j in range(i+1, n):
            if A[smallest] > A[j]:
                smallest = j
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
    return A


if __name__ == "__main__":
    A = [100, 8, 9, 7, 6, 4, 6, 8, 4, 231, 884, 54]
    selection_sort(A)
