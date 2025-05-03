import sys
import math

# Read input
T = int(input().strip())
P = int(input().strip())
for case in range(T):
    # Read test case
    test_case = []
    for _ in range(100):
        test_case.append([int(x) for x in input().strip()])
    
    # Initialize variables
    cheater = None
    cheater_skill = 0
    cheater_difficulty = 0
    
    # Loop through each player and question
    for i in range(1, 101):
        for j in range(1, 10001):
            # Calculate probability of correct answer
            prob = math.exp(-(test_case[i-1][j-1] - test_case[100][j-1])) / (1 + math.exp(-(test_case[i-1][j-1] - test_case[100][j-1])))
            
            # Check if player is cheater
            if random.random() < 0.5:
                cheater = i
                cheater_skill = sum(test_case[i-1]) / 10000
                cheater_difficulty = sum(test_case[100][j-1]) / 10000
    
    # Output answer
    print("Case #{}: {}".format(case+1, cheater))