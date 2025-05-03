import sys

# Read input from stdin
T = int(input())

for t in range(T):
    # Read number of rooms and maximum number of operations from input
    N, K = map(int, input().split())
    
    # Initialize passages as a dictionary to store the number of passages for each room
    passages = {}
    
    # Process up to K + 1 exchanges
    for i in range(K + 1):
        # Read current room and number of passages from input
        r, p = map(int, input().split())
        
        # Update passages dictionary with the new information
        if r not in passages:
            passages[r] = p
        else:
            passages[r] += p
    
    # Estimate the number of passages based on the information in passages
    E = sum(passages.values()) / 2
    
    # Output the estimate
    print(E)