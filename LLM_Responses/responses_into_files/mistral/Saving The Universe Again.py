import re

def min_hacks(d, p):
    if d >= sum([1 if c == 'C' else 0 for c in p]) or not p:
        return "IMPOSSIBLE"

    hacks = 0
    i = 1
    while i < len(p) and (hacks + sum([1 if j > i and p[j] != p[i-1] and p[j-1] == p[i-1] else 0 for j in range(i, len(p))]) <= d - sum([1 if c == 'C' else 0 for c in p[:i]])):
        hacks += 1
        i += 2
    return str(hacks)

T = int(input())
for _ in range(T):
    D, P = input().split()
    D, P = int(D), P.replace(' ', '')
    print(f"Case #{_+1}: {min_hacks(D, P)}")