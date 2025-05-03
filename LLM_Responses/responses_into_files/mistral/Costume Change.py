import sys
input = sys.stdin.readline

def solve(N):
    grid = [list(map(int, input().split())) for _ in range(N)]
    colors, materials = set(), set()
    for row in grid:
        colors.add(row[0])
        materials.add(-row[0] if row[0] < 0 else row[0])
    n_costumes = len(colors) * len(materials)
    changes = 0
    for i in range(N):
        colors_in_row, materials_in_row = set(), set()
        for j in range(N):
            c, m = grid[i][j]
            colors_in_row.add(colors.pop(c-1))
            materials_in_row.add(materials.pop(-m))
        if len(colors_in_row) > 1:
            changes += len(colors_in_row) - 1
        if len(materials_in_row) > 1:
            changes += len(materials_in_row) - 1
    return changes

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print('Case #{}: {}'.format(t, solve(N)))