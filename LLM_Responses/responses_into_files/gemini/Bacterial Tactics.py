def solve():
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]

    empty_cells = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '.':
                empty_cells.append((r, c))

    if not empty_cells:
        return 0

    winning_moves = 0
    for r, c in empty_cells:
        # Try H colony
        new_grid_h = [row[:] for row in grid]
        new_grid_h[r][c] = 'H'
        valid_h = True
        for i in range(C):
            if new_grid_h[r][i] == '#':
                break
            if new_grid_h[r][i] == 'H':
              continue
            new_grid_h[r][i] = 'H'

        
        if all(all(cell != '.' for cell in row) for row in new_grid_h):
          continue

        #Try V colony

        new_grid_v = [row[:] for row in grid]
        new_grid_v[r][c] = 'V'
        valid_v = True
        for i in range(R):
            if new_grid_v[i][c] == '#':
                break
            if new_grid_v[i][c] == 'V':
              continue
            new_grid_v[i][c] = 'V'

        if all(all(cell != '.' for cell in row) for row in new_grid_v):
          continue
        
        winning_moves +=2

    return winning_moves


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")