import sys
from collections import defaultdict
input = sys.stdin.readline

def max_lead(R, G):
    dp = [0] + [float('-inf') * len(G) for _ in range(len(R))]
    graph = defaultdict(list)
    for r1, r2 in R:
        graph[r1].append(r2)
        graph[r2].append(r1)

    for i in reversed(range(1, len(R))):
        for j in range(i+1, len(R)):
            if dp[j] > dp[i]:
                for k in graph[i]:
                    if dp[k] < dp[j] - 1:
                        dp[k] = max(dp[k], dp[j] - 1 + G[i])

    return max(dp)

T = int(input())
for _ in range(T):
    M, *R = map(int, input().split())
    G = list(map(int, input().split()))
    print("Case #{}: {}".format(_+1, max_lead(R, G)))


This Python program takes the number of test cases and the metal formulas as input, and calculates the maximum amount of lead that can be obtained by using the given metal formulas and the initial amounts of metals in the treasury. The program uses dynamic programming to find the optimal solution for each test case.