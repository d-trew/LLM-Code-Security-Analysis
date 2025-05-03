import sys
input = sys.stdin.readlines

def rotate_beam(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[None] * cols for _ in range(rows)]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "-":
                new_grid[i][j] = "|"
            elif cell == "|":
                new_grid[i][j] = "-"
    return new_grid

def shoot_beam(grid, beam_shooter):
    rows, cols = len(grid), len(grid[0])
    direction = [(0, 1), (1, 0)] if beam_shooter == "|" else [(0, -1), (-1, 0)]
    x, y = beam_shooter[0], beam_shooter[1]
    grid[x][y] = "#"
    while 0 <= x < rows and 0 <= y < cols:
        if grid[x][y] in ["#", "."]:
            break
        x += direction[0][0]
        y += direction[0][1]
    return grid

def solve(grid):
    beam_shooters = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == "-" or cell == "|"]
    rotations = 0
    for bs in beam_shooters:
        grid = shoot_beam(grid, bs)
        for _ in range(4):
            grid = rotate_beam(grid)
            grid = shoot_beam(grid, bs)
            if any(cell == "#" for row in grid for cell in row):
                break
        else:
            rotations += 1
    return "POSSIBLE\n" + "\n".join("".join(row) for row in grid) if not any(cell == "#" for row in grid for cell in row) else "IMPOSSIBLE"

T = int(input()[0].strip())
for _ in range(1, T+1):
    R, C = map(int, input()[0].strip().split(" "))
    grid = [list(input()[i].strip() for i in range(1, 1 + R)]
    print(f"Case #{_}: {solve(grid)}")