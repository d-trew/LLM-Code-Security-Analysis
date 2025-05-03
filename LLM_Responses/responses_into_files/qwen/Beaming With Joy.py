def rotate_beam_shooter(grid, row, col):
    if grid[row][col] == '/':
        return '|'
    elif grid[row][col] == '\\':
        return '-'
    elif grid[row][col] == '-':
        return '\\'
    elif grid[row][col] == '|':
        return '/'
    else:
        return grid[row][col]

def is_valid(grid, R, C):
    visited = [[False for _ in range(C)] for _ in range(R)]
    
    def dfs(x, y, dx, dy):
        if x < 0 or x >= R or y < 0 or y >= C:
            return True
        if grid[x][y] == '#':
            return False
        if visited[x][y]:
            return False
        visited[x][y] = True
        
        if grid[x][y] == '-' or grid[x][y] == '|':
            nx, ny = x + dx, y + dy
        elif grid[x][y] == '/':
            nx, ny = x - dy, y + dx
        elif grid[x][y] == '\\':
            nx, ny = x + dy, y - dx
        
        return dfs(nx, ny, dx, dy)
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '-' or grid[i][j] == '|' or grid[i][j] == '/' or grid[i][j] == '\\':
                if not dfs(i, j, 0, 1) and not dfs(i, j, 1, 0) and not dfs(i, j, 0, -1) and not dfs(i, j, -1, 0):
                    return False
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.':
                if not any(dfs(i + dx, j + dy, dx, dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                    return False
    
    return True

def solve(grid, R, C):
    if not is_valid(grid, R, C):
        return "IMPOSSIBLE"
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '-' or grid[i][j] == '|' or grid[i][j] == '/' or grid[i][j] == '\\':
                rotated_grid = [row[:] for row in grid]
                rotated_grid[i] = list(rotate_beam_shooter(rotated_grid, i, j))
                if is_valid(rotated_grid, R, C):
                    return "POSSIBLE\n" + '\n'.join(''.join(row) for row in rotated_grid)
    
    return "IMPOSSIBLE"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R, C = map(int, data[index:index+2])
        index += 2
        grid = [data[index + i] for i in range(R)]
        index += R
        
        result = solve(grid, R, C)
        results.append(result)
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    main()