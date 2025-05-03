from collections import deque

def bfs(i, j, grid):
    n = len(grid)
    m = len(grid[0])
    initials = set()
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        if 0 <= x < n and 0 <= y < m and grid[x][y] != '?':
            initials.add(grid[x][y])
            grid[x][y] = '?'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                q.append((x + dx, y + dy))
    return initials

def solve(R, C, grid):
    children = set()
    for i in range(R):
        for j in range(C):
            if grid[i][j] != '?':
                children.add(grid[i][j])
                grid[i][j] = '?'
                initials = bfs(i, j, grid)
                assert len(initials) == 1
                child = list(children)[0]
                for x in range(R):
                    for y in range(C):
                        if grid[x][y] == '?':
                            grid[x][y] = child
    return grid

T = int(input().strip())
for t in range(1, T + 1):
    R, C = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]
    grid = solve(R, C, grid)
    print('Case #{}:'.format(t))
    for row in grid:
        print(''.join(row))