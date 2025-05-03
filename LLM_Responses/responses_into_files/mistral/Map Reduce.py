import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    R, C, D = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]
    start_x, start_y = 0, 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start_x, start_y = i, j

    visited = [[False] * C for _ in range(R)]
    queue = [(start_x, start_y, 0)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        x, y, steps = queue.pop(0)

        if grid[x][y] == 'F':
            if steps <= D:
                print(f'Case #{_ + 1}: POSSIBLE')
                for row in grid:
                    print(''.join(row))
                continue
            else:
                print(f'Case #{_ + 1}: IMPOSSIBLE')
                continue

        if not visited[x][y]:
            visited[x][y] = True

            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#':
                    queue.append((nx, ny, steps + 1))

    print(f'Case #{_ + 1}: IMPOSSIBLE')