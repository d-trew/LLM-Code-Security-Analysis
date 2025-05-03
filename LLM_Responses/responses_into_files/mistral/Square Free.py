import sys
from collections import defaultdict
input = sys.stdin.readlines

def solve(r, c, s, d):
    if r * r != c * c:
        return "IMPOSSIBLE"

    diags = defaultdict(int)
    for i in range(r):
        diags[i] = sum([s[j] for j in range(min(i, r - i - 1), max(0, r - i))])

    if sum(diags.values()) != c:
        return "IMPOSSIBLE"

    matrix = [['.' for _ in range(c)] for _ in range(r)]

    for i in range(r):
        for j, diag in enumerate(s[min(i, r - i - 1):max(0, r - i)]):
            matrix[i][j + diag] = '/' if diag > d[j] else '\\'

    return '\n'.join(''.join(row) for row in matrix)

T = int(input()[0])
for _ in range(1, T+1):
    r, c = map(int, input().split())
    s = list(map(int, input().split()))
    d = list(map(int, input().split()))
    print(f'Case #{_}: {solve(r, c, s, d)}')