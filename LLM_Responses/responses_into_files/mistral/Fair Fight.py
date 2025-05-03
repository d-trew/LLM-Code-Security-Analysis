import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        C = list(map(int, input().split()))
        D = list(map(int, input().split()))
        swords = sorted(list(set(C + D)))
        count = 0
        for i in range(len(swords) - 1):
            for j in range(i + 1, min(N, i + K + 1)):
                if max((sum([c[i] for c in enumerate(C) if swords[i] == c[0])) - max((sum([d[j] for d in enumerate(D) if swords[j] == d[0]])), 0),
                       max((sum([d[j] for d in enumerate(D) if swords[i] == d[0]]) - max((sum([c[i] for c in enumerate(C) if swords[j] == c[0]]), 0))):
                   <= K:
                    count += 1
        print("Case #{}: {}".format(_ + 1, count))

solve()