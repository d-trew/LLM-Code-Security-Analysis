# Import necessary libraries here


def countMistakes(N): # Function to calculate mistakes of each player based on game history and rules defined above        for i, (Mi , Ci) in enumerate((zip([int() for _  in range N], [ int ()] )), start = 1 ):
            if ((i %2 ==0)) & not(Ci - Mi==-3): # If odd turn but no consecutive numbers are found then mistake by player A is incremented.        else:    pass   # No mistakes if even numbered turns and there's a pair of adjacent,consecutive tiles in the game board
            if ((i %2 ==1)) & not(Ci - Mi==3): # If odd turn but no consecutive numbers are found then mistake by player B is incremented.        else:    pass   # No mistakes if even numbered turns and there's a pair of adjacent,consecutive tiles in the game board
            if i %2 == 1 :  a += (Ci - Mi==-3) # Incrementing total number pf errors for Player A based on rule defined above.        else:    pass   # No mistakes if even numbered turns and there's a pair of adjacent,consecutive tiles in the game board
            if i %2 == 0 :  b += (Ci - Mi==3) # Incrementing total number pf errors for Player B based on rule defined above.        else:    pass   # No mistakes if even numbered turns and there's a pair of adjacent,consecutive tiles in the game board

print(f"Case #{i}: {a}  {b}")