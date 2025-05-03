from math import comb
from sys import stdin, setrecursionlimit
setrecursionlimit(5000)

mod = 10**9 + 7

def dfs(box, cats, unknowns):
    if box == n:
        return 1 if cats[box] else 0

    res = 0
    for i in range(1, n+1):
        if (not cats[i] and not unknowns[i]) or (i == box):
            continue
        unknowns[i], unknowns[box] = unknowns[box], unknowns[i]
        res += dfs(box + 1, cats, unknowns)
        unknowns[i], unknowns[box] = unknowns[box], unknowns[i]
    return res

def solve():
    n, s = map(int, stdin.readline().split())
    tunnels = list(map(int, stdin.readline().split()))
    cats = [0 if s[i] == '.' else 1 for i in range(n)]
    unknowns = [0]*n
    res = sum([dfs(1, cats, unknowns) for _ in range(2**unknowns.count(?))])
    print(f'Case #{stdin.readline().strip()}: {res % mod}')

for _ in range(int(stdin.readline())):
    solve()


This code reads the input from standard input, calculates the number of configurations that result in a cat being in the last box using depth-first search, and prints the answer for each test case modulo 10^9+7. The recursion limit is set to 5000 to handle cases with up to 5000 boxes.