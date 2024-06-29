def matrix_multiplication(p):
    matrix_no = len(p)-1
    m = [[0 for _ in range(matrix_no)] for _ in range(matrix_no)]
    s = [[0 for _ in range(matrix_no)] for _ in range(matrix_no)]

    for l in range(2, matrix_no+1):
        for i in range(1, matrix_no-l+2):
            j = i+l-1
            m[i-1][j-1] = float("inf")
            for k in range(i, j):
                q = m[i-1][k-1]+m[k][j-1]+p[i-1]*p[k]*p[j]
                if m[i-1][j-1] > q:
                    m[i-1][j-1] = q
                    s[i-1][j-1] = k
    return m, s


def display_mutliplication(s, i, j):
    if (i == j):
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        display_mutliplication(s, i, s[i][j]-1)
        display_mutliplication(s, s[i][j], j)
        print(")", end="")


arr = [5, 4, 6, 2, 7]
m, s = matrix_multiplication(arr)
for i in range(len(m)):
    print(m[i])
for i in range(len(s)):
    print(s[i])

display_mutliplication(s, 0, len(arr)-2)
