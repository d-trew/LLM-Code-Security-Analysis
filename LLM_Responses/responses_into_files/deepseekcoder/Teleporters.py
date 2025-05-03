import heapq
from collections import defaultdict

def l1_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

def shortest_path(graph, start, end):
    queue = [(0, start)]
    distances = {start: 0}
    previous = {}
    while queue:
        (dist, current) = heapq.heappop(queue)
        if dist != distances[current]: continue
        for neighbor in graph[current]:
            old_distance = distances.get(neighbor, None)
            new_distance = distances[current] + l1_distance(current, neighbor)
            if old_distance is None or new_distance < old_distance:
                distances[neighbor] = new_distance
                previous[neighbor] = current
                heapq.heappush(queue, (new_distance, neighbor))
    path = []
    while end is not None:
        path.append(end)
        end = previous.get(end, None)
    return distances, path[::-1] if start in distances else []

def solve():
    T = int(input())
    for tc in range(T):
        N = int(input())
        points = [tuple(map(int, input().split())) for _ in range(N+2)]
        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if l1_distance(points[i], points[j]) <= 3:
                    graph[points[i]].append(points[j])
                    graph[points[j]].append(points[i])
        distances, path = shortest_path(graph, points[0], points[-1])
        print("Case #{}: {}".format(tc+1, 'IMPOSSIBLE' if not path else len(path)-1))

solve()