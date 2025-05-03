import sys
from random import randint

def estimate_passages(N, K):
    passages = {}
    for _ in range(K + 1):
        R_i, P_i = map(int, input().split())
        if R_i not in passages:
            passages[R_i] = []
        passages[R_i].append(P_i)
    
    total_passages = sum(passages.values()) // 2
    estimate = randint(total_passages * 2 // 3, total_passages * 4 // 3)
    print(estimate)

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    estimate_passages(N, K)