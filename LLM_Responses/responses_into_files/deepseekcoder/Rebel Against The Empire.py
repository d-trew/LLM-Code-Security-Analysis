import heapq
from math import sqrt

def calc_distance(x, y):
    return sqrt(x**2 + y**2)

def solve():
    T = int(input())
    for t in range(1, T+1):
        N, S = map(int, input().split())
        asteroids = [tuple(map(int, input().split())) for _ in range(N)]
        
        edges = [[] for _ in range(N)]
        for i in range(N-1):
            for j in range(i+1, N):
                x1, y1, z1 = asteroids[i]
                x2, y2, z2 = asteroids[j]
                dist = calc_distance((x2 - x1) * S, (y2 - y1) * S) + \
                       calc_distance((z2 - z1) * S, (sqrt(3)*S)**2 - 2*dist)
                edges[i].append((j, dist))
                edges[j].append((i, dist))
        
        max_heap = [(0, 0)]
        min_distance = [float('inf')] * N
        while max_heap:
            d, u = heapq.heappop(max_heap)
            if d < min_distance[u]:
                min_distance[u] = d
                for v, w in edges[u]:
                    alt = d + w
                    if alt < min_distance[v]:
                        heapq.heappush(max_heap, (alt, v))
        
        print("Case #{}: {}".format(t, min_distance[-1]))

solve()