import math
from heapq import heappush, heappop

def dijkstra(n, s):
    dist = [float('inf')] * n
    dist[s] = 0
    pq = []
    heappush(pq, (0, s))

    while pq:
        cur_dist, cur_node = heappop(pq)

        if dist[cur_node] < cur_dist:
            continue

        for next_node, (x, y, z, vx, vy, vz) in enumerate(astoids):
            next_pos = [x + vx * cur_dist, y + vy * cur_dist, z + vz * cur_dist]
            if 0 <= next_pos[0] < n and 0 <= next_pos[1] < n and 0 <= next_pos[2] < n:
                next_dist = math.sqrt((next_pos[0] - cur_node) ** 2 + (next_pos[1] - dist[cur_node][1]) ** 2 + (next_pos[2] - dist[cur_node][2]) ** 2)
                if next_dist + dist[cur_node] < dist[next_node]:
                    dist[next_node] = dist[cur_node] + next_dist
                    heappush(pq, (dist[next_node], next_node))

    return dist[-1]

def solve():
    T = int(input().strip())
    for _ in range(T):
        N, S = map(int, input().split())
        astoids = [list(map(float, input().split())) for _ in range(N)]
        start_pos, goal_pos = 0, 1
        dist_to_start = 0
        dist_to_goal = math.sqrt((goal_pos[0] - start_pos[0]) ** 2 + (goal_pos[1] - start_pos[1]) ** 2 + (goal_pos[2] - start_pos[2]) ** 2)
        max_jump = dist_to_goal

        for i in range(S):
            dist = dijkstra(N, start_pos)
            if dist[-1] <= S:
                max_jump = min(max_jump, dist[goal_pos])
                start_pos = goal_pos
                dist_to_start, dist_to_goal = dist_to_goal, math.sqrt((start_pos[0] - goal_pos[0]) ** 2 + (start_pos[1] - goal_pos[1]) ** 2 + (start_pos[2] - goal_pos[2]) ** 2)

        print(f"Case #{_+1}: {max_jump:.4f}")