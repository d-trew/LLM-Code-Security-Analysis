import sys

# Read input from standard input
T = int(sys.stdin.readline())
N = 200
for i in range(T):
    # Read number of customers for this test case
    Nc = int(sys.stdin.readline())
    
    # Initialize a list to store the probabilities of each flavor being liked by a customer
    probs = [0.005] * N
    
    # Read and process each customer's preferences
    for j in range(Nc):
        # Read number of flavors liked by this customer
        D = int(sys.stdin.readline())
        
        # Read the IDs of the flavors liked by this customer
        ids = [int(x) for x in sys.stdin.readline().split()]
        
        # Update the probabilities of each flavor being liked by a customer
        for k in range(D):
            probs[ids[k]] += 1.0 / Nc
    
    # Initialize a list to store the lollipops sold to each customer
    sold = [-1] * Nc
    
    # Process each customer's preferences and sell them a lollipop
    for j in range(Nc):
        # Read the number of flavors liked by this customer
        D = int(sys.stdin.readline())
        
        # Read the IDs of the flavors liked by this customer
        ids = [int(x) for x in sys.stdin.readline().split()]
        
        # Find a flavor that is liked by this customer and not already sold to another customer
        for k in range(D):
            if probs[ids[k]] > 0:
                sold[j] = ids[k]
                break
    
    # Write the lollipop sold to each customer to standard output
    for j in range(Nc):
        sys.stdout.write(str(sold[j]) + "\n")