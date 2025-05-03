import sys
from heapq import heappush, heappop

def dijkstra(graph, source):
    dist = [float('inf')] * (len(graph) + 1)
    dist[source] = 0
    prio_queue = []
    heappush(prio_queue, (0, source))

    while prio_queue:
        d, u = heappop(prio_queue)
        if dist[u] < d:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(prio_queue, (dist[v], v))

    return dist[2:]

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        C, D = map(int, sys.stdin.readline().split())
        graph = [[] for _ in range(C + 1)]
        times = list(map(int, sys.stdin.readline().split()))
        times = sorted([-x if x < 0 else x for x in times[1:]])
        for _ in range(D):
            u, v = map(int, sys.stdin.readline().split())
            graph[u].append((v, 1))
            graph[v].append((u, 1))

        result = dijkstra(graph, 1)
        print("Case #{}: {}".format(_ + 1, ' '.join(str(x) for x in result)))

solve()


This code reads the number of test cases T from the standard input. For each test case, it reads the number of computers C and direct connections D, then it initializes a graph with adjacency list representation. After that, it reads the timestamps for each computer except for the source one (computer 1) and sorts them in ascending order. Then it iterates through all direct connections and adds them to the graph as bidirectional edges with weight 1. Finally, it uses Dijkstra's algorithm to find the shortest paths from the source computer to all other computers and prints the result for each test case.