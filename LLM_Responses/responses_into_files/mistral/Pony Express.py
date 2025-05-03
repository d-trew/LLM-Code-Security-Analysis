import sys
from math import inf
from heapq import heappush, heappop

def dijkstra(dist, cities, edges):
    h = []
    for c in cities:
        dist[c] = float('inf')
        heappush(h, (0, c))

    while h:
        d, u = heappop(h)
        if d > dist[u]: continue
        for v, w in edges[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(h, (dist[v], v))
    return dist

def pony_express(cities, edges):
    N = len(cities)
    start, end = 1, N
    dist = [0] * (N+1)
    dist[start] = 0
    dist[end] = 0
    edges.append([(start, -1, float('inf'))] + [[(end, -1, 0)]])

    for i in range(2, N):
        dist[i] = dijkstra(dist, cities, edges)[i]

    return dist[end]

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, E = map(int, sys.stdin.readline().split())
        cities = list(range(1, N+1))
        edges = []
        for _ in range(E):
            u, v, w = map(int, sys.stdin.readline().split())
            edges.append((u, [(v, -1, w)]))
        print("Case #{}: {}".format(_+1, pony_express(cities, edges)))

main()


This code reads the number of test cases and then iterates through each case to calculate the minimum time necessary for each delivery. It uses Dijkstra's algorithm to find the shortest path from the starting city to the destination city, taking into account that the horses have a maximum total distance they can travel before becoming too tired. The input is read line by line, and the output is printed for each test case in the format specified in the problem description.