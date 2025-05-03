Here's a Python solution using depth-first search (DFS) and backtracking to solve the problem. This program will print out "IMPOSSIBLE" if it is not possible to visit each cell exactly once, otherwise it will print "POSSIBLE" followed by the path of cells visited in order.


def dfs(grid, r, c, R, C):
    dx = [0, 1, -1, 0, 1, -1, 1, -1]
    dy = [1, 0, 0, -1, 1, -1, -1, 1]
    
    for i in range(8):
        nx, ny = r + dx[i], c + dy[i]
        
        if R > nx >= 0 and C > ny >= 0 and grid[nx][ny]:
            grid[nx][ny] = 0
            
            if dfs(grid, nx, ny, R, C): return True
    
    return False

def solve():
    T = int(input())
    
    for case in range(1, T + 1):
        R, C = map(int, input().split())
        
        grid = [[1]*C for _ in range(R)]
        
        print('Case #{}: '.format(case), end='')
        
        if dfs(grid, 0, 0, R, C): print('IMPOSSIBLE')
        else: print('POSSIBLE\n' + '\n'.join([' '.join(map(str, cell)) for cell in grid]))

This code starts at the top left corner of the grid and tries to find a path through the rest of the cells. If it can't do this (it returns True), then it knows that there is no valid path from the current cell back to the start. It keeps track of which cells have been visited by setting them to 0 in the grid.