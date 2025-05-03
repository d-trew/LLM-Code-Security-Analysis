from math import gcd
import sys
input = sys.stdin.read().splitlines()
T = int(input[0])
for _ in range(1, T+1):
    R, C, N, D = map(int, input[1].split())
    grid = [list(map(int, line.split())) for line in input[2:]]

    # Initialize a 2D array to store the brightness values of each cell
    dp = [[0] * C for _ in range(R)]

    # Fill the cells that have already been painted by Cody-Jamal
    for i, row in enumerate(grid):
        for j, brightness in enumerate(row):
            dp[i][j] = brightness % (109 + 7)

    # Iterate through the remaining cells and find the maximum sum that can be obtained without violating the rules
    max_sum = 0
    for i in range(R):
        for j in range(C):
            if dp[i][j] == 0:
                # Check all possible brightness values for the cell (dp[i][j])
                for k in range(1, 109):
                    diff = max([abs(dp[i][j-1] - k), abs(dp[i][j+1] - k), abs(dp[i-1][j] - k), abs(dp[i+1][j] - k)])
                    if diff <= D:
                        # If the new brightness value does not violate the rules, update the maximum sum and the dp array
                        temp_sum = (dp[i][j-1] + dp[i][j+1] + dp[i-1][j] + dp[i+1][j] - 4 * k) % (109 + 7)
                        if temp_sum > max_sum:
                            max_sum = temp_sum
                            dp[i][j] = k

    print(f"Case #{_}: {"IMPOSSIBLE" if max_sum == 0 else (max_sum % (109 + 7))}")