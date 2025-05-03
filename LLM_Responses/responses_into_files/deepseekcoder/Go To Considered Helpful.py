from collections import deque
import sys
input = sys.stdin.readline

def bfs(matrix, start_point):
    queue = deque([start_point + (0,)])  # BFS with depth tracking
    visited = {start_point}
    while queue:
        point, d = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny, nd = point[0] + dx, point[1] + dy, d + 1
            if not (0 <= nx < len(matrix[0]) and 0 <= ny < len(matrix)) or matrix[ny][nx] == '#': continue
            if (nx, ny) in visited:
                if visited[(nx, ny)][1] >= d - 1:  # If the point is already visited with a shorter or equal depth
                    queue.append(((nx, ny), nd))
                    visited[(nx, ny)] = (point, nd)
            else:
                queue.append(((nx, ny), nd))
                visited[(nx, ny)] = (point, nd)
    return visited

def path_reconstruction(visited, end):
    point, d = visited[end]
    path = [end]
    while point != start_point:
        point, _ = visited[point]
        path.append(point)
    return list(reversed(path))

T = int(input())
for t in range(1, T+1):
    R, C = map(int, input().split())
    matrix = [list(map(str, input())) for _ in range(R)]
    start_point = end_point = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'M': 
                start_point, matrix[i][j] = (j, i), '.'
            elif matrix[i][j] == 'N': 
                end_point, matrix[i][j] = (j, i), '.'
    if not start_point or not end_point: 
        print(f'Case #{t}: IMPOSSIBLE')
        continue
    visited = bfs(matrix, start_point)
    path = path_reconstruction(visited, end_point) if end_point in visited else None
    print(f"Case #{t}: {len(path) - 1 if path else 'IMPOSSIBLE'}")