import math

def count_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    def get_neighbours(r, c):
        neighbours = []
        
        if r > 0 and grid[r-1][c] == grid[r][c]:
            neighbours.append((r-1, c))
        if r < rows - 1 and grid[r+1][c] == grid[r][c]:
            neighbours.append((r+1, c))
        if c > 0 and grid[r][c-1] == grid[r][c]:
            neighbours.append((r, c-1))
        if c < cols - 1 and grid[r][c+1] == grid[r][c]:
            neighbours.append((r, c+1))
            
        return neighbours
    
    def dfs(cell, visited):
        cell_count = 1
        
        for r, c in get_neighbours(*cell):
            if (r,c) not in visited:
                visited.add((r,c))
                cell_count += dfs((r,c), visited)
                
        return cell_count
    
    max_pattern = 0
    
    for r in range(rows):
        for c in range(cols):
            pattern = dfs((r,c), set())
            
            if pattern > max_pattern:
                max_pattern = pattern
                
    return max_pattern
        
def main():
    T = int(input())
    
    for i in range(1, T+1):
        R, C = map(int, input().split())
        grid = [list(input()) for _ in range(R)]
        max_size = math.log(count_patterns(grid), 2) + 1
        
        print("Case #%d: %d" % (i, max_size))

if __name__ == "__main__":
    main()