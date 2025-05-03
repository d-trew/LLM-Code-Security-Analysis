def solve():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        grid = []
        for _ in range(N):
            row = list(map(int, input().split()))
            grid.append(row)
        
        changes = 0
        for i in range(N):
            color_wool = [False]*N
            color_cotton = [False]*N
            for j in range(N):
                if grid[i][j] < 0:  # Wool costume
                    if color_wool[-grid[i][j]]:
                        changes += 1
                        grid[i][j] *= -1
                    else:
                        color_wool[-grid[i][j]] = True
                elif grid[i][j] > 0:  # Cotton costume
                    if color_cotton[grid[i][j]-1]:
                        changes += 1
                        grid[i][j] *= -1
                    else:
                        color_cotton[grid[i][j]-1] = True
        
        for j in range(N):
            color_wool = [False]*N
            color_cotton = [False]*N
            for i in range(N):
                if grid[i][j] < 0:  # Wool costume
                    if color_wool[-grid[i][j]-1]:
                        changes += 1
                        grid[i][j] *= -1
                    else:
                        color<｜begin▁of▁sentence｜>color_woo