def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(n):
        index = int(A[i] * n)
        B[index].append(A[i])

    for i in range(n):
        B[i].sort()

    sorted_array = []
    for i in range(n):
        sorted_array.extend(B[i])  # Concatenate the sorted buckets

    return sorted_array


if __name__ == "__main__":
    A = [0.100, 0.8, 0.9, .07, 0.6, 0.4, 0.6, 0.8, 0.4, 0.231, 0.884, 0.54]
    B = bucket_sort(A)
    print(B)
