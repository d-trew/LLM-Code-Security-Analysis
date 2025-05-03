import math

# Read input
T = int(input())
N = int(input())
B = int(input())
P = int(input())

# Initialize variables
scores = []
total_score = 0

# Process each test case
for i in range(T):
    # Initialize towers
    towers = [[] for _ in range(N)]
    
    # Read input and place blocks
    for j in range(N*B):
        d = int(input())
        i = 1
        while len(towers[i-1]) == B:
            i += 1
        towers[i-1].append(d)
    
    # Calculate score and add to total
    for tower in towers:
        score = sum([int(digit) for digit in str(tower)])
        scores.append(score)
        total_score += score
    
# Print result
if total_score >= P:
    print("1")
else:
    print("-1")