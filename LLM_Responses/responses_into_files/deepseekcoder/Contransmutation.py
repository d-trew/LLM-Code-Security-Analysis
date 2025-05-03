import sys
from heapq import *

def solve():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        g = list(map(int, input().split()))
        edges = [[] for _ in range(n+1)]
        deg = [0] * (n + 1)
        dp = [[0] * 2 for _ in range(n+1)]
        res = 0
        
        for i in range(m):
            a, b = map(int, input().split())
            edges[b].append(a)
            deg[a] += 1
            
        q = [i for i in range(1, n+1) if not deg[i]]
        
        while q:
            new_q = []
            for u in q:
                dp[u][0] = max(dp[v][1] + g[v-1] for v in edges[u]) % MOD
                dp[u][1] = max(dp[u][1], dp[u][0] if u == 1 else (max(dp[v][1] for v in edges[u]) + g[u-1]))
                res = max(res, dp[u][1])
                
                deg[u] -= 1
                for v in edges[u]:
                    if deg[v] == 0:
                        new_q.append(v)
            q = new_q
            
        print(res % MOD)
        
solve()