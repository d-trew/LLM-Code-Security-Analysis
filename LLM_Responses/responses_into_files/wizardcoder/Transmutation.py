import sys

T = int(input()) # Read number of test cases
for i in range(1, T+1):
    M = int(input()) # Number of metals known in the world
    formulas = {}
    
    for j in range(M):
        R1, R2 = map(int, input().split()) # Read formula for metal j
        formulas[R1] = R2
        
    G = list(map(int, input().split())) # List of grams of each metal
    
    lead_grams = 0
    while any([G[x] > 0 for x in range(len(G)-1)]): # While there are still metals left to convert into lead
        max_metal = -1 # Keep track of the metal with most grams available
        
        for j in range(1, M+1): # Find the metal that has the highest amount available and use it to create lead
            if G[j] > 0:
                max_metal = j
                
        if max_metal == -1: # If there are no more metals left to convert into lead, break out of loop
            break
        
        for metal in formulas.keys():
            if metal != max_metal and G[metal] > 0: # Find the next metal that can be used to create lead with the available metal
                G[max_metal] -= 1
                G[formulas[max_metal]] += 1
                lead_grams += 1
    
    print("Case #{}: {}".format(i, lead_grams)) # Output the result for each test case