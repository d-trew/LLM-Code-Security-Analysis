import math

def solve(N, D):
    # Calculate the minimum number of cuts needed for each diner
    min_cuts = []
    for i in range(D):
        min_cuts.append(math.ceil(2 * math.pi * (N - 1) / N))
    
    # Initialize the total number of cuts to 0
    total_cuts = 0
    
    # Loop through each diner and calculate the minimum number of cuts needed for that diner
    for i in range(D):
        total_cuts += min_cuts[i]
    
    return total_cuts

# Test cases
cases = int(input())
for case in range(1, cases + 1):
    N, D = map(int, input().split())
    print("Case #" + str(case) + ": " + str(solve(N, D)))