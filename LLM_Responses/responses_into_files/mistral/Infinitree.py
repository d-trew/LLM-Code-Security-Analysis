import sys
from collections import defaultdict
input = sys.stdin.readline

def lca(x, y):
    if x > y:
        x, y = y, x
    while x != y:
        x = parents[x]
        for p in (2 * x, 2 * x + 1):
            if p <= N and colors[p] == L[x]:
                x = p
            elif p <= N and colors[p] == R[x]:
                x = parents[p]
    return x

def dfs(node, par):
    global depth
    nonlocal parents, depth, colors
    parents[node] = par
    depth[node] = depth[par] + 1
    if node != 1:
        colors[node] = (colors[2 * par], colors[2 * par + 1])

def solve():
    N, A, B = map(int, input().split())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    parents = [0] + [0] * N
    depth = [0] * (N + 1)
    colors = [0] * (N + 1)
    dfs(1, 0)

    ans = float('inf')
    for i in range(2, N + 1):
        if depth[i] != depth[B]:
            continue
        lca_node = lca(A, i)
        if depth[lca_node] == depth[B]:
            ans = min(ans, depth[lca_node] - depth[i])
        else:
            ans = min(ans, depth[lca_node] + depth[B] - 2 * depth[i])
    print(f"Case #{T+1}: {ans}")

T = int(input())
for _ in range(T):
    solve()


This Python program reads the input from standard input, finds the Lowest Common Ancestor (LCA) of two nodes using Depth-First Search (DFS), and calculates the distance between the given two nodes using their depths. The tree is represented as a list of colors for each node, where the root has color 1 and each non-root node's children have colors L and R respectively. The program then uses this representation to find the LCA and calculate the distance between the nodes.