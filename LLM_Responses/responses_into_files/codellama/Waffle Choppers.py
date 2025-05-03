import sys

def solve(R, C, H, V):
    # Check if the waffle is empty
    if R * C == 0:
        return "IMPOSSIBLE"
    
    # Check if the number of horizontal and vertical cuts are valid
    if H < 1 or V < 1 or H + 1 > R or V + 1 > C:
        return "IMPOSSIBLE"
    
    # Initialize a dictionary to keep track of the chocolate chip counts
    chip_count = {}
    
    # Iterate through each cell in the waffle and update the chip count dictionary
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "@":
                chip_count[(i, j)] = 1
            else:
                chip_count[(i, j)] = 0
    
    # Iterate through each horizontal cut and update the chip count dictionary
    for i in range(H):
        start = (i + 1) * C // (H + 1) - 1
        end = (i + 2) * C // (H + 1)
        for j in range(start, end):
            chip_count[(i, j)] += 1
    
    # Iterate through each vertical cut and update the chip count dictionary
    for j in range(V):
        start = (j + 1) * R // (V + 1) - 1
        end = (j + 2) * R // (V + 1)
        for i in range(start, end):
            chip_count[(i, j)] += 1
    
    # Check if the total number of chocolate chips is divisible by the number of diners
    if sum(chip_count.values()) % (H + 1) * (V + 1) == 0:
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"
    
# Read input
R, C, H, V = map(int, sys.stdin.readline().split())
grid = []
for _ in range(R):
    grid.append(list(sys.stdin.readline().rstrip()))

# Print output
print("Case #1: " + solve(R, C, H, V))