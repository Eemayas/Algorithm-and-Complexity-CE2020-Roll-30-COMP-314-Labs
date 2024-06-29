import math


def LCS_memorization(P, S, m, n, memo):
    if m == len(P) or n == len(S):
        return 0

    if memo[m][n] != 0:
        return memo[m][n]

    if P[m] == S[n]:
        memo[m][n] = 1+LCS_memorization(P, S, m+1, n+1, memo)
        return memo[m][n]
    else:
        memo[m][n] = max([LCS_memorization(P, S, m, n+1, memo), LCS_memorization(P, S, m+1, n, memo)])
        return memo[m][n]

def lcs_tabulation(X, Y):
    m = len(X)+1
    n = len(Y)+1

    table = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if X[i-1] == Y[j-1]:
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = max([table[i][j-1], table[i-1][j]])
    print("Tabulation")
    print("=========================\n")
    for i in range(len(table)):
        print(table[i])
    return table[m-1][n-1]


X = "stratosphere"
Y = "atmosphere"

memo = [[0 for _ in range(len(Y)+1)]for _ in range(len(X)+1)]
print(LCS_memorization(X, Y, 0, 0, memo))
print("Memorization")
print("=========================\n")
for i in range(len(memo)):
    print(memo[i])

print(lcs_tabulation(X, Y))
