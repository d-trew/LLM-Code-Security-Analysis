import sys
sys.setrecursionlimit(10**6)
def dfs(grid, r, c, visited):
    if grid[r][c] == '|':
        return True
    elif (r, c) in visited:
        return False
    visited.add((r, c))
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and dfs(grid, nr, nc, visited):
            return True
    return False
    
def solve_case(input_str):
    lines = input_str.split('\n')
    num_cases = int(lines[0])
    for i in range(num_cases):
        R, C = map(int, lines[i*2+1].strip().split())
        grid = [list(lines[j+2]) for j in range(R)]
        
        visited = set()
        beam_covered = False
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.' and not dfs(grid, r, c, visited):
                    beam_covered = True
                    break
        
        print("Case #{}".format(i+1), "POSSIBLE" if beam_covered else "IMPOSSIBLE")
    
def main():
    input_str = sys.stdin.read()
    solve_case(input_str)
    
if __name__ == '__main__':
    main()