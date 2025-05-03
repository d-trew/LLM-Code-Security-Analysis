import sys

def solve(R, C):
    # Initialize the largest pattern size as 0
    max_pattern = 0
    
    # Iterate through each cell in the dream grid
    for i in range(R):
        for j in range(C):
            # If the current cell is white or black, and its neighbors are also white or black, then it forms a pattern
            if grid[i][j] == "W" and (grid[i-1][j] == "W" or grid[i+1][j] == "W" or grid[i][j-1] == "W" or grid[i][j+1] == "W") and (grid[i-1][j-1] == "W" or grid[i+1][j+1] == "W"):
                # Get the size of the pattern by counting the number of cells in it
                pattern_size = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if grid[k][l] == "W":
                            pattern_size += 1
                
                # Update the largest pattern size if the current pattern is larger than the previous one
                max_pattern = max(max_pattern, pattern_size)
    
    return max_pattern

# Read the number of test cases
T = int(input())

# Loop through each test case
for case in range(1, T+1):
    # Read the dimensions of the dream grid
    R, C = map(int, input().split())
    
    # Initialize a 2D array to store the dream grid
    grid = [[" " for _ in range(C)] for _ in range(R)]
    
    # Read the dream grid and store it in the array
    for i in range(R):
        for j in range(C):
            grid[i][j] = input()
    
    # Find the largest pattern size in the starting dream grid
    max_pattern = solve(R, C)
    
    # Output the answer
    print("Case #" + str(case) + ": " + str(max_pattern))