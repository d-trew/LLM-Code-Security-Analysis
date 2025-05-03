import sys

def solve(B, S):
    # Initialize a dictionary to store the number of times each building appears in the parade route
    building_count = {i: 0 for i in range(1, B+1)}
    
    # Iterate through each slide and update the building count accordingly
    for i in range(S):
        u, v = map(int, input().split())
        building_count[u] += 1
        building_count[v] += 1
    
    # Check if all buildings appear the same number of times in the parade route
    for i in range(1, B+1):
        if building_count[i] != S:
            return "IMPOSSIBLE"
    
    # Return the length of the parade route
    return len(building_count) + 1

# Read input
B = int(input())
S = int(input())

# Solve the problem and print output
print("Case #1:", solve(B, S))