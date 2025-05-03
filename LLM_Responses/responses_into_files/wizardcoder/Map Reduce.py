import sys
sys.setrecursionlimit(10**6)

def dfs(grid, r, c, d, visited):
    if grid[r][c] == 'F':
        return d + 1
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr, nc) not in visited:
            visited.add((nr, nc))
            return max(dfs(grid, nr, nc, d + 1, visited), key=lambda x: x[1])
    
    return None

def is_possible(grid, r, c, d):
    visited = set()
    result = dfs(grid, r, c, 0, visited)
    if not result or result[1] == d:
        return True
    else:
        return False
    
def remove_walls(grid, start_r, start_c):
    possible_walls = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                new_grid = [row.copy() for row in grid]
                new_grid[i][j] = '.'
                if is_possible(new_grid, start_r, start_c):
                    possible_walls.append((i, j))
    
    return possible_walls

def main():
    T = int(input())
    for case in range(1, T + 1):
        R, C, D = map(int, input().split())
        grid = [list(input()) for _ in range(R)]
        
        start_r, start_c = None
        finish_r, finish_c = None
        
        for i in range(len(grid)):
            for j in range(len(grid[0]):
                if grid[i][j] == 'S':
                    start_r, start_c = i, j
                elif grid[i][j] == 'F':
                    finish_r, finish_c = i, j
        
        possible_walls = remove_walls(grid, start_r, start_c)
        if any([d for d in range(D) if d != D and (finish_r - d, finish_c) in possible_walls]):
            print("Case #{}: POSSIBLE".format(case))
            
            for i in range(len(grid)):
                for j in range(len(grid[0]):
                    if (i, j) not in possible_walls:
                        sys.stdout.write(grid[i][j])
                    else:
                        sys.stdout.write('.')
                print()
        else:
            print("Case #{}: IMPOSSIBLE".format(case))
        
if __name__ == "__main__":
    main()