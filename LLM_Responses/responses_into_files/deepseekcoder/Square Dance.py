def calculate_interest(R, C, grid):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # up, down, left, right
    round = 0
    while True:
        eliminated = set()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0 or any((r+dr, c+dc) not in grid or grid[(r+dr, c+dc)] == 0 for (dr, dc) in directions):
                    continue
                neighbors = [grid[(r+dr, c+dc)] for (dr, dc) in directions if 0 <= r+dr < R and 0 <= c+dc < C]
                avg_skill = sum(neighbors)/len(neighbors)
                if grid[r][c] < avg_skill:
                    eliminated.add((r, c))
        if not eliminated:
            break
        for r, c in eliminated:
            grid[(r, c)] = 0
        round += 1
    return sum(sum(row) for row in grid)*round

T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    grid = {(r, c): int(val) for r in range(R) for c, val in enumerate(input().split())}
    print('Case #{}: {}'.format(tc, calculate_interest(R, C, grid)))