import sys
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(n, edges):
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    queue = [(0, 1)]

    while queue:
        d, u = heapq.heappop(queue)

        if dist[u] < d:
            continue

        for v, c, capacity, price in edges[u]:
            if capacity > 0 and dist[v] > dist[u] + price:
                dist[v] = dist[u] + price
                heapq.heappush(queue, (dist[v], v))

    return dist

def solve():
    n = int(input())
    edges = defaultdict(list)

    for _ in range(n - 1):
        u, v, c, p = map(int, input().split())
        edges[u].append((v, c, n, p))

    skiers = dijkstra(n, edges)
    max_skiers = max(skiers)
    min_expense = sum(d * (max_skiers - skiers[i]) for i in range(2, n + 1))
    print(f'Case #{solve_count}: {max_skiers} {min_expense}')
    solve_count += 1

solve_count = 0
T = int(input())
for _ in range(T):
    solve()


This code reads the number of test cases, T, and then iterates through each test case. For each test case, it reads the number of rest points, N, and creates a graph using adjacency list representation. Then it calculates the shortest path from the starting point (1) to all other points using Dijkstra's algorithm, where the cost is the price or bounty of the slope multiplied by the difference between the maximum number of skiers the slope can accommodate and the actual number of skiers using that slope. Finally, it finds the maximum number of skiers that can be put on the mountain and calculates the minimum expense for having that maximum number of skiers ski at least one slope each. The output is in the format specified in the problem statement.