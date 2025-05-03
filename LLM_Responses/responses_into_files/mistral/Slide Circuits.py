import sys
input = sys.stdin.readline

def make_adj(n, edges):
    adj = [[] for _ in range(n+1)]
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)
    return adj

def fun_state(adj, n, k):
    circuits = []
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, adj, visited, k, circuits)
    return len(circuits) == k

def dfs(cur, adj, visited, k, circuits):
    visited[cur] = True
    for nbr in adj[cur]:
        if not visited[nbr]:
            dfs(nbr, adj, visited, k, circuits)
            circuits[-1].append(nbr)
    if len(circuples[-1]) == k and all(visited):
        circuits.pop()

def solve():
    T = int(input())
    for _ in range(T):
        B, S, N = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(S)]
        adj = make_adj(B, edges)
        operations = []
        for _ in range(N):
            op, l, r, m = input().split()
            operations.append((op[0].upper(), int(l), int(r), int(m)))
        fun = True
        for i, (operation, l, r, m) in enumerate(operations):
            if operation == 'E':
                if not fun_state(adj, B, len(set(range(l, r+1, m)) & {x for x in range(1, B+1) if x not in adj[0]})):
                    fun = False
                    break
            elif operation == 'D':
                fun = fun_state(adj, B, len(set(range(l, r+1, m)) & {x for x in range(1, B+1) if x in adj[0]}))
                if not fun:
                    print(f'Case #{i+1}: X')
                    break
        else:
            print(f'Case #{i+1}: {min([x for x in range(1, B+1) if x not in adj[0]])}')

solve()