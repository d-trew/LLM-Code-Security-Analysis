Here's the Python code that solves this problem using the concept of graph theory and depth-first search (DFS):


def dfs(v, color, adj_list):
    if color[v] != 0: return 1 if color[v] == 2 else 0
    color[v] = 2
    for u in adj_list[v]:
        if not dfs(u, color, adj_list): return False
    color[v] = 1
    return True

def solve():
    N = int(input())
    F = list(map(int, input().split()))
    F.insert(0, 0)
    adj_list = [[] for _ in range(N+1)]
    for i in range(1, N+1): adj_list[F[i]].append(i)
    color = [0] * (N + 1)
    res = 0
    for v in range(1, N+1): 
        if dfs(v, color, adj_list): res += 1
    return res

T = int(input())
for tc in range(1, T+1): print("Case #{}: {}".format(tc, solve()))

This code first reads the input and constructs an adjacency list representation of the directed graph. Then it performs a depth-first search on each node that has not been visited yet to find cycles in the graph (which means some kids cannot be in the circle). The number of nodes that have no cycle is the answer to this problem.