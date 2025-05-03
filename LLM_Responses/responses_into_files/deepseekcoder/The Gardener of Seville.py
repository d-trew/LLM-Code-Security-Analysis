def solve_maze(R, C, lovers):
    if len(lovers) != R*C - 1:
        return "IMPOSSIBLE"
    
    maze = [['/' for _ in range(2 * (R + C))] for _ in range(R)]
    
    def dfs(i, j):
        if i < 0 or i >= R or j < 0 or j >= 2*(R+C) or maze[i][j] != '/':
            return False
        
        maze[i][j] = 'X'
        if (j == len(maze[0]) - 1) or dfs(i, j + 2):
            return True
            
        if i < R - 1 and maze[i+1][j] != '/':
            maze[i][j] = '\\'
            return False
        
        if dfs(i + 1, j + 2) or (j > 0 and dfs(i, j - 2)):
            return True
            
        maze[i][j] = '/'
        return False
    
    for i in range(R):
        dfs(i, 0)
        
    if any('X' in row for row in maze):
        return "IMPOSSIBLE"
    
    return '\n'.join([''.join([cell for cell in row]) for row in maze]) + '\n'

T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    lovers = list(map(int, input().split()))
    result = solve_maze(R, C, lovers)
    
    print("Case #{}: {}".format(tc, result))