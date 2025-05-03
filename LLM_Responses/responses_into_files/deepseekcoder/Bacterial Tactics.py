def count_winning_moves(grid, r, c):
    def dfs(x, y, dx, dy):
        nonlocal grid
        x += dx
        y += dy
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return True
        if grid[x][y] == '.':
            grid[x][y] = 'V' if dx else 'H'
            if dfs(x, y, dx, dy):
                return True
            grid[x][y] = '.'
        elif grid[x][y].isalpha():
            return False
        return False

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if dfs(i, j, dx, dy):
                        count += 1
    return count

T = int(input())
for case in range(1, T + 1):
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]
    print('Case #{}: {}'.format(case, count_winning_moves(grid, R, C)))