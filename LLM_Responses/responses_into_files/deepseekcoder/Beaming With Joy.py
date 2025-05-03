T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]
    possible = True
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '.':
                has_beam = False
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    while 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] == '|':
                            possible = False
                        elif grid[nr][nc] in ['/\\']:
                            break
                        elif grid[nr][nc] == '#':
                            nr, nc = r + dr, c + dc
                            break
                        has_beam = True
                        break
                if not has_beam:
                    possible = False
    print(f"Case # {_+1}: {'POSSIBLE' if possible else 'IMPOSSIBLE'}")
    if possible:
        for row in grid:
            print(''.join(row))