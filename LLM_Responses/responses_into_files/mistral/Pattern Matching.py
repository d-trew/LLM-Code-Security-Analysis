import re

def find_match(patterns):
    if not patterns:
        return "*"

    pattern = ""
    for i, p in enumerate(patterns):
        if len(p) > 104 or any(c != "*" and c.isalpha() for c in p):
            return "*"
        if not pattern:
            pattern += p[1:]
        elif p[:len(pattern)] != pattern[:-1]:
            return "*"
        pattern = p[:len(pattern)] + pattern[1:]

    return pattern.upper()

def solve():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        patterns = [input().upper() for _ in range(N)]
        print(f"Case #{t}: {find_match(patterns)}")

solve()