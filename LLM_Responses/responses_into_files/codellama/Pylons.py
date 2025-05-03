import sys

def solve(R, C):
    # Initialize a dictionary to keep track of visited cells
    visited = {}

    # Iterate through all rows and columns
    for i in range(1, R+1):
        for j in range(1, C+1):
            # If the current cell has not been visited, visit it
            if (i, j) not in visited:
                # Add the current cell to the visited dictionary
                visited[(i, j)] = True

                # Check if the current cell shares a row, column, or diagonal with any previous cells
                for k in range(1, R+1):
                    for l in range(1, C+1):
                        if (k, l) in visited and abs(i-k) <= 1 and abs(j-l) <= 1:
                            # If the current cell shares a row, column, or diagonal with any previous cells, return "IMPOSSIBLE"
                            return "IMPOSSIBLE"

    # Return "POSSIBLE" if all cells have been visited
    return "POSSIBLE"

# Read input
T = int(sys.stdin.readline())
for t in range(T):
    R, C = map(int, sys.stdin.readline().split())
    result = solve(R, C)
    print("Case #{}".format(t+1))
    print(result)