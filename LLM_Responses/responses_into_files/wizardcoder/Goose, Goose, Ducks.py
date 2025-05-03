import math
import sys
from collections import defaultdict

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2

def is_feasible(N, M, S, meetings, statements):
    ducks = set()
    geese = set(range(1, N+1))
    for i in range(M):
        xi, yi, ci = meetings[i]
        for j in range(S):
            ai, bi, ui, vi, di = statements[j]
            if distance(xi, yi, ui, vi) <= ci ** 2:
                ducks.add(ai)
                geese.discard(ai)
                ducks.discard(bi)
                geese.discard(bi)
    return len(ducks), len(geese)

def main():
    T = int(input())
    for i in range(1, T+1):
        N, M, S = map(int, input().split())
        meetings = [tuple(map(int, input().split())) for _ in range(M)]
        statements = [(tuple(map(int, input().split())) for _ in range(S)]
        min_ducks, max_geese = is_feasible(N, M, S, meetings, statements)
        print("Case #{}: {}".format(i, min_ducks))
        
if __name__ == "__main__":
    main()