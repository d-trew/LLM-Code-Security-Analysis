import sys

def solve(input):
    # Read input
    R, C = map(int, input().split())
    grid = []
    for _ in range(R):
        grid.append(list(sys.stdin.readline().strip()))
    
    # Initialize output grid with original grid
    output_grid = [[grid[r][c] for c in range(C)] for r in range(R)]
    
    # Replace ? with letters from A to Z
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '?':
                output_grid[r][c] = chr(ord('A') + (r * C + c) % 26)
    
    # Print output grid
    print("Case #1:")
    for r in range(R):
        print(''.join(output_grid[r]))

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        solve(input())