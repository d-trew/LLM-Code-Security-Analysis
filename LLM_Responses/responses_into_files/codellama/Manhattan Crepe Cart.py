#!/bin/python3
import sys
input = sys.stdin.readline
T=int(input())
for t in range(1, T+1):
    P,Q=map(int, input().split())
    people = []
    for _ in range(P):
        Xi,Yi,Di = map(int, input().split())
        people.append((Xi, Yi, Di))
    max_x = 0
    max_y = 0
    for x, y, d in people:
        if d == 'N':
            max_y = max(max_y, y)
        elif d == 'S':
            max_y = min(max_y, y)
        elif d == 'E':
            max_x = max(max_x, x)
        elif d == 'W':
            max_x = min(max_x, x)
    print("Case #%d: %d %d" % (t, max_x, max_y))