from math import gcd
from collections import defaultdict

def mod_pow(a, b, m):
    a %= m
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b >>= 1
    return res

def max_lead(R, G):
    n = len(G)
    graph = defaultdict(list)
    inv = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in R[i]:
            if j == i: continue
            graph[j].append((i, 1))
            inv[i] = mod_pow(-1, G[i], 1000000007)
    q = [(0, 0)] + enumerate(G)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i, g in q:
        if i == 0 or g == 0: continue
        for j in graph[i]:
            (k, w) = j
            dp[k][w] = max(dp[k][w], dp[i][0] + w * inv[k])
        dp[i][0] += g
    ans = 0
    for i in range(1, n + 1):
        for j in graph[i]:
            (k, w) = j
            ans = (ans + dp[k][w]) % 1000000007
    return ans

def solve():
    T = int(input())
    for t in range(T):
        M = int(input())
        R = [[] for _ in range(M + 1)]
        for i in range(1, M + 1):
            r1, r2 = map(int, input().split())
            R[i].append((r1 - 1, r2 - 1))
            if r1 != i and r2 != i:
                R[r1].append((i - 1, 1))
        G = list(map(int, input().split()))
        print("Case #{}: {}".format(t + 1, max_lead(R, G) % 1000000007))

solve()


This Python code reads the number of test cases T, then for each test case it reads the number of metals M, their transformations and the initial amounts of metals in the treasury. It uses dynamic programming to find the maximum amount of lead that can be obtained using the given transformations. The function max_lead calculates the maximal amount of lead by iterating through all possible metals and considering the transformations that involve lead or the current metal. It also calculates the inverse of each metal's weight modulo 109+7, which is used to calculate the optimal number of times to apply a transformation. The result is the remainder when the maximal amount of lead is divided by 1000000007.