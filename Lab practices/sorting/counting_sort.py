def counting_sort(A):
    if A == []:
        return []
    max_element = max(A)
    C = [0]*(max_element+1)
    for i in range(len(A)):
        C[A[i]] = C[A[i]]+1
    for i in range(len(C)-1):
        C[i+1] = C[i]+C[i+1]
    B = [0]*len(A)
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]]-1
    return B


if __name__ == "__main__":
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    B = counting_sort(A)
    print(B)
