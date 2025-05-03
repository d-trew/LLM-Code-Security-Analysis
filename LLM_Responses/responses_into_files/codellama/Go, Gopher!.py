import sys

# Read input from standard input
n = int(input())

# Loop through each test case
for i in range(n):
    # Read the minimum required prepared rectangular area for this test case
    A = int(input())

    # Initialize variables to keep track of the deployed cells and their coordinates
    deployed_cells = set()
    row, col = -1, -1

    # Deploy the gopher up to 1000 times
    for j in range(1000):
        # Generate a random cell coordinate within the boundaries of the matrix
        r = randint(2, 999)
        c = randint(2, 999)

        # Check if the generated coordinate has already been deployed
        if (r, c) not in deployed_cells:
            row, col = r, c
            break

    # If the gopher did not prepare any cell, stop the test case
    if row == -1 or col == -1:
        print(-1, -1)
        continue

    # Prepare the cell that was chosen by the gopher
    deployed_cells.add((row, col))

    # Check if the set of prepared cells forms a rectangle of area at least A
    area = len(deployed_cells)
    if area >= A:
        print(0, 0)
        break

    # If the test case is not solved yet, send out another cell location to deploy
    else:
        print(row, col)

# If the test case is solved, print a message indicating that
if area >= A:
    print("Solved!")