import sys
def solve(R, C, D, N):
    grid = [[0]*C for _ in range(R)]
    for i in range(N):
        r, c, val = map(int, input().split())
        grid[r-1][c-1] = val
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                min_val = max_val = grid[r][c]
                for nr in range(max(0, r-D), min(R, r+D+1)):
                    for nc in range(max(0, c-D), min(C, c+D+1)):
                        if (r != nr or c != nc) and grid[nr][nc] > 0:
                            min_val = min(min_val, grid[nr][nc])
                            max_val = max(max_val, grid[nr][nc])
                if max_val - min_val <= D:
                    for nr in range(max(0, r-D), min(R, r+D+1)):
                        for nc in range(max(0, c-D), min(C, c+D+1)):
                            if (r != nr or c != nc) and grid[nr][nc] > 0:
                                grid[r][c] = (grid[r][c] + grid[nr][nc]) % 109+7
                else:
                    return "IMPOSSIBLE"
    
    total = sum(grid[i][j] for i in range(R) for j in range(C))
    return str(total % 109+7)

T = int(input())
for i in range(T):
    R, C, D, N = map(int, input().split())
    print("Case #{}: {}".format(i+1, solve(R, C, D, N)))