import heapq

def bfs(r, c):
    queue = [(0, r, c)]
    visited = set((r, c))
    path = []
    while queue:
        dist, row, col = heapq.heappop(queue)
        if len(path) == r * c:
            return 'POSSIBLE'
        for nr, nc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]:
            nr += row
            nc += col
            if 1 <= nr <= r and 1 <= nc <= c and (nr, nc) not in visited:
                path.append((nr, nc))
                visited.add((nr, nc))
                heapq.heappush(queue, (dist + 1, nr, nc))
    return 'IMPOSSIBLE'

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    print(f'Case #{"%d" % (_+1)}: POSSIBLE')
    for r, c in bfs(R, C):
        print(f'{r} {c}')