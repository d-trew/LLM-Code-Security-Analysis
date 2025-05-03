import sys
input = sys.stdin.readlines

def assign_initial(R, C):
    grid = [list(c.strip()) for c in input().splitlines()]
    n_letters = len(set(grid[0]))
    assignments = [['?'] * C for _ in range(R)]

    def dfs(r, c, initial):
        if r < 0 or r == R or c < 0 or c == C:
            return
        if grid[r][c] != '?' and assignments[r][c] != initial:
            return

        assignments[r][c] = initial
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dfs(r + dr, c + dc, initial)

    for i, initial in enumerate(set(grid[0])):
        dfs(0, 0, initial)

    for r in range(R):
        print(' '.join(assignments[r]))

T = int(input().strip())
for _ in range(T):
    R, C = map(int, input().split())
    assign_initial(R, C)