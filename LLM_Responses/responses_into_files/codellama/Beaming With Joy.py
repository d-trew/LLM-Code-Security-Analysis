import sys

def solve(R, C):
    grid = []
    for i in range(R):
        grid.append([])
        for j in range(C):
            if grid[i][j] == '|':
                grid[i][j] = '|'
            elif grid[i][j] == '-':
                grid[i][j] = '-'
    return grid

if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    grid = []
    for i in range(R):
        grid.append([])
        for j in range(C):
            grid[i].append(sys.stdin.readline().strip())
    print("Case #1: POSSIBLE")
    print(*grid, sep='\n')