import sys

def solve(R, C, M):
    # Initialize a grid to represent the map
    grid = [[0 for _ in range(C)] for _ in range(R)]

    # Fill the grid with the given information
    for i in range(R):
        for j in range(C):
            if input_map[i][j] == 'S':
                grid[i][j] = 1
            elif input_map[i][j] == 'T':
                grid[i][j] = 2

    # Initialize the maximum number of turrets that can be destroyed
    max_turrets = 0

    # Iterate through each row and column of the grid
    for i in range(R):
        for j in range(C):
            # If the current cell is a soldier, check if it can destroy any turrets
            if grid[i][j] == 1:
                # Check if there are any turrets in the same row or column as the soldier
                for k in range(R):
                    for l in range(C):
                        if grid[k][l] == 2 and abs(k - i) <= M and abs(l - j) <= M:
                            # If there is a turret, check if the soldier can reach it within M moves
                            if abs(k - i) <= M and abs(l - j) <= M:
                                # If the soldier can reach the turret within M moves, destroy it
                                grid[k][l] = 0
                                max_turrets += 1

    return max_turrets

# Read input from stdin
input_map = []
for _ in range(int(sys.stdin.readline())):
    # Get the dimensions of the map and the number of unit moves each soldier can make
    R, C, M = map(int, sys.stdin.readline().split())

    # Read the map from stdin
    input_map = []
    for _ in range(R):
        input_map.append(list(sys.stdin.readline().strip()))

    # Print the maximum number of turrets that can be destroyed
    print("Case #1:", solve(R, C, M))