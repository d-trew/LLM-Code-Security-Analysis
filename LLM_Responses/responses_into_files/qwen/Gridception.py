def find_largest_pattern(grid):
    R, C = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def is_valid(x, y):
        return 0 <= x < R and 0 <= y < C
    
    def dfs(x, y, color, path, visited):
        if (x, y) in visited:
            return
        visited.add((x, y))
        path.append((x, y))
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and grid[nx][ny] == color:
                dfs(nx, ny, color, path, visited)
    
    def get_patterns():
        patterns = set()
        for i in range(R):
            for j in range(C):
                if (i, j) not in visited:
                    path = []
                    dfs(i, j, grid[i][j], path, visited)
                    pattern = tuple(sorted(path))
                    patterns.add(pattern)
        return patterns
    
    visited = set()
    patterns = get_patterns()
    
    max_pattern_size = 0
    for pattern in patterns:
        if len(pattern) >= max_pattern_size:
            max_pattern_size = len(pattern)
    
    return max_pattern_size

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R = int(data[index])
        C = int(data[index + 1])
        grid = [data[index + 2 + i] for i in range(R)]
        index += R + 2
        
        result = find_largest_pattern(grid)
        results.append(f"Case #{_+1}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()