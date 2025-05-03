def find_max_turrets(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[[-1]*4 for _ in range(cols)] for _ in range(rows)]
    moves = [(-1, 0, 2), (1, 0, 0), (0, -1, 3), (0, 1, 1)]
    
    def dfs(x, y, prev_move):
        if not ((0 <= x < rows) and (0 <= y < cols)):
            return float('inf'), None
        if grid[x][y] in 'ST' or dp[x][y][prev_move] != -1:
            return dp[x][y][prev_move]
        
        res, path = min((dfs(x+dx, y+dy, move) for dx, dy, move in moves if move != (prev_move+2)%4), default=(float('inf'), None))
        dp[x][y][prev_move] = 1 + res if grid[x][y] == 'T' and path is not None else float('inf')
        
        return dp[x][y][prev<｜begin▁of▁sentence｜>c