# This is a comment and will be ignored by the Python interpreter

def assign_stations(R, C, S):
    # Initialize a matrix to represent the city grid
    grid = [[0 for _ in range(C)] for _ in range(R)]

    # Loop through each station and its patrol distance
    for i in range(S):
        Ri, Ci, Di = map(int, input().split())
        # Get the row and column of the current station
        r, c = Ri-1, Ci-1
        # Get the maximum patrol distance from the current station
        d = Di+1
        # Loop through each block in the grid
        for i in range(R):
            for j in range(C):
                # Calculate the distance between the current block and the station
                dist = abs(i-r) + abs(j-c)
                # If the distance is less than or equal to the patrol distance, assign the block to the station
                if dist <= d:
                    grid[i][j] = i+1

    # Initialize variables to keep track of the number of blocks assigned and the minimum/maximum number of blocks assigned
    num_blocks_assigned = 0
    min_num_blocks_assigned = float('inf')
    max_num_blocks_assigned = -float('inf')

    # Loop through each block in the grid and count the number of stations that can patrol it
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0:
                num_blocks_assigned += 1
                min_num_blocks_assigned = min(min_num_blocks_assigned, num_blocks_assigned)
                max_num_blocks_assigned = max(max_num_blocks_assigned, num_blocks_assigned)

    # Return the difference between the minimum and maximum number of blocks assigned as the solution
    return max_num_blocks_assigned - min_num_blocks_assigned