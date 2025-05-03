import sys
from heapq import *
input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    dist[0] = 0
    hq = [(0, 0)]
    while hq:
        d, now = heappop(hq)
        if dist[now] < d: continue
        for next_node, cost in graph[now]:
            next_d = d + cost
            if next_d < dist[next_node]:
                dist[next_node] = next_d
                heappush(hq, (next_d, next_node))

def solve():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        graph = [[] for _ in range(N)]
        dist = [INF] * N
        for i in range(N - 1):
            u, v, s, c = map(int, input().split())
            graph[u - 1].append((v - 1, -c)) # negative cost because we are minimizing
        dijkstra()
        ans = sum([-i for i in dist])
        print("Case #{}: {}".format(t,ans))
        
solve()