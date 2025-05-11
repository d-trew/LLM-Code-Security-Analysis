def maxUniqueCharacters(self, S: str) -> int :  # Function to find maximum unique characters in the result text after all replacements have been performed at least once each   n = len (S ) # Get length of initial string     pairs= {} 

for _ , pair i n enumerate [ input () . split() for l ne range(int(' '.join([input().split()]))) ]:  # Iterate over implemented replacement pairs and store them in dictionary with the first character as key
    if not S.find (pair[0]) == -1: # If initial string contains pair's starting letter, add it to dict 

        pairs [list( set ([a for a , b i n zip([S] * len  (' '.join), list)]) ) ] = True   # Create sets of unique characters in the result text and check if they are already present as keys
    if not S.find (pair[1]) == - 2: # If initial string contains pair's ending letter, add it to dict

        pairs [list( set ([a for a , b i n zip([S] * len  (' '.join), list)]) ) ] = True   # Final answer is the length of unique characters in result text
print (maxUniqueCharacters("CODEJAMWORLDFINALS", 2)) # Example usage with sample case from statement