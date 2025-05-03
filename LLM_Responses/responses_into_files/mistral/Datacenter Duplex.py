import sys
input = sys.stdin.readlines

def solve(grid):
    R, C = len(grid), len(grid[0])
    if not any(all(c == 'A' for c in row) or all(c == 'B' for c in row) for row in grid):
        return "IMPOSSIBLE"

    connected_A, connected_B = set(), set()
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == 'A':
                connected_A.add((i, j))
            elif c == 'B':
                connected_B.add((i, j))

    def dfs(x, y, visited):
        if (x, y) in visited or x < 0 or y < 0 or x >= R or y >= C:
            return False
        if (x, y) in connected_A:
            visited.add((x, y))
            for nx, ny in ((x + 1, y + 1), (x + 1, y), (x, y + 1)):
                dfs(nx, ny, visited)
            return True
        elif (x, y) in connected_B:
            visited.add((x, y))
            for nx, ny in ((x - 1, y + 1), (x - 1, y), (x, y - 1)):
                dfs(nx, ny, visited)
            return True
        return False

    grid_copy = [row[:] for row in grid]
    for i, j in connected_A:
        if not dfs(i, j, set()):
            return "IMPOSSIBLE"

    connections = []
    for i in range(R - 1):
        for j in range(C - 1):
            if grid_copy[i][j] == '/' and grid_copy[i + 1][j + 1] == '\\':
                grid_copy[i][j], grid_copy[i + 1][j + 1] = '.', '.'
                connections.append('\\')
            elif grid_copy[i][j] == '\\' and grid_copy[i + 1][j + 1] == '/':
                grid_copy[i][j], grid_copy[i + 1][j + 1] = '.', '.'
                connections.append('\\')
            elif grid_copy[i][j] == '.' and grid_copy[i + 1][j + 1] in ('/', '\\'):
                grid_copy[i][j], grid_copy[i + 1][j + 1] = '/', '\\' if grid_copy[i + 1][j + 1] == '/' else '\\', '/'
    return "\n".join([".".join(row) for row in grid_copy]) + "\n" + "\n".join(connections)

T = int(input()[0].strip())
for _ in range(T):
    R, C = map(int, input()[0].split())
    grid = [list(input()[i].strip().upper()) for i in range(1, 1 + R)]
    print("Case #{}: {}".format(_+1, solve(grid)))