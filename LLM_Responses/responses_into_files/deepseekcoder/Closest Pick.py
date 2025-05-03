import sys
from math import inf

def pancake_win_probability(N, K, P):
    min_dist = inf
    for i in range(1, K+1):
        if i not in P:
            dist = sum(abs(i - p) for p in P)
            if dist < min_dist:
                min_dist = dist
    return min_dist / (K * N)

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    print(f"Case #{_+1}: {pancake_win_probability(N, K, P):.6f}")