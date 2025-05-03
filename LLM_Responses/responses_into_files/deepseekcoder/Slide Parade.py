from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    B, S = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(S):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [0]*(B+1)
    path = []
    
    def dfs(node):
        if not visited[node]:
            visited[node] = 1
            for i in graph[node]:
                if not visited[i]:
                    path.append((node,i))
                    dfs(i)
                    
    dfs(1)
    
    if len(path) < B-1:
        return "IMPOSSIBLE"
        
    path = [(1,2)] + path[:B-2] + [(1,2)][::-1]
    res = [1]*(len(path)*2+1)
    
    for i in range(len(path)):
        u, v = path[i]
        res[i], res[-(i+3)] = (u,v) if i%2 else (v,u)
        
    return " ".join([str(i) for i in [1] + res])
    
T = int(input())
for t in range(1, T + 1):
    print("Case #{}: {}".format(t, solve()))