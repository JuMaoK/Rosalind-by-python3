'''
Title: Longest Increasing Subsequence
URL: http://rosalind.info/problems/lgis/

Given: A positive integer n≤10000 followed by a permutation π of length n.
Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

Reference:
https://en.wikipedia.org/wiki/Longest_increasing_subsequence
https://stackoverflow.com/questions/3992697/longest-increasing-subsequence
'''

with open(r'rosalind_lgis.txt') as f:
    read_data = f.read().split()
    n = int(read_data[0])
    pai = list(map(int, read_data[1:]))

def longest_increasing_subsequence(X):
    """Returns the Longest Increasing Subsequence in the Given List/Array"""
    N = len(X)
    P = [0] * N
    M = [0] * (N + 1)
    L = 0
    for i in range(N):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if (X[M[mid]] < X[i]):
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        if (newL > L):
            L = newL

    S = []
    k = M[L]
    for i in range(L - 1, -1, -1):
        S.append(X[k])
        k = P[k]
    return S[::-1]

incr = longest_increasing_subsequence(pai)
print(*incr)
