def counting_sort_radix(A, exp):
    n = len(A)
    C = [0]*(10)
    for i in range(n):
        index = (A[i]//exp) % 10
        C[index] = C[index]+1
    for i in range(1, len(C)):
        C[i] = C[i-1]+C[i]
    B = [0]*n
    for i in range(n-1, -1, -1):
        index = (A[i]//exp) % 10
        B[C[index]-1] = A[i]
        C[index] -= 1
    return B


def radix_sort(A):
    max_element = max(A)
    count = 0
    while max_element > 0:
        count += 1
        max_element = max_element//10
    exp = 1
    for d in range(count):
        A = counting_sort_radix(A, exp*(pow(10, d)))

    return A


if __name__ == "__main__":
    A = [5151, 84894984, 949494, 949, 94]
    print(radix_sort(A))
