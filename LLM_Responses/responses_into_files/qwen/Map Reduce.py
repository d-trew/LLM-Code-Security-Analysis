from collections import deque

def bfs(grid, start, end):
    R, C = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    distance = {start: 0}
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return distance[(x, y)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#' and (nx, ny) not in distance:
                queue.append((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1
    
    return float('inf')

def remove_walls(grid, start, end, D):
    R, C = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def is_valid(grid):
        return bfs(grid, start, end) <= D
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '#':
                new_grid = [row[:] for row in grid]
                new_grid[i][j] = '.'
                if is_valid(new_grid):
                    return True, new_grid
    return False, None

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R, C, D = map(int, data[index:index+3])
        index += 3
        grid = [list(data[index + i]) for i in range(R)]
        start = None
        end = None
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 'S':
                    start = (i, j)
                elif grid[i][j] == 'F':
                    end = (i, j)
        
        possible, new_grid = remove_walls(grid, start, end, D)
        results.append("POSSIBLE" if possible else "IMPOSSIBLE")
        if possible:
            for row in new_grid:
                results.append(''.join(row))
    
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}")

if __name__ == "__main__":
    solve()