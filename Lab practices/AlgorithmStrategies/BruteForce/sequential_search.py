def sequential_search(A, key):
    n = len(A)
    if n == 0:
        return -1
    i = 0
    while i < n and A[i] != key:
        i = i+1
    if (i == n):
        return -1
    return i


if __name__ == "__main__":
    A = [89, 74, 97, 37, 86, 84, 53, 46, 78, 56, 80, 54, 41, 65, 54,
         94, 94, 27, 76, 75, 74, 80, 93, 63, 16, 44, 35, 19, 2, 83]
    print(sequential_search(A,874))
