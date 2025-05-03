import sys

def solve(n_patterns):
    # Initialize a list to store all possible names
    names = []
    
    # Loop through each pattern
    for pattern in patterns:
        # Split the pattern into individual characters
        chars = pattern.split('')
        
        # Create a set of characters that appear in the pattern
        char_set = set(chars)
        
        # Check if there are any asterisks in the pattern
        has_asterisk = '*' in char_set
        
        # If there are no asterisks, then we can append the entire pattern to the list of names
        if not has_asterisk:
            names.append(pattern)
            
        # Otherwise, we need to generate all possible names that match the pattern
        else:
            # Get the indices of the asterisks in the pattern
            asterisk_indices = [i for i, char in enumerate(chars) if char == '*']
            
            # Loop through each index of the asterisk
            for i in asterisk_indices:
                # Get the characters before and after the asterisk
                prefix = chars[:i]
                suffix = chars[i+1:]
                
                # Generate all possible names that match the pattern by combining the prefix and suffix
                for name in generate_names(prefix, suffix):
                    names.append(name)
    
    # Return a single name that matches all patterns if there is one, or '*' otherwise
    if len(names) == 1:
        return names[0]
    else:
        return '*'

def generate_names(prefix, suffix):
    # Initialize a list to store all possible names
    names = []
    
    # Loop through each character in the prefix and suffix
    for p in prefix:
        for s in suffix:
            # Combine the characters to form a name
            name = p + s
            
            # Add the name to the list of possible names if it is at most 104 letters long
            if len(name) <= 104:
                names.append(name)
    
    # Return the list of possible names
    return names

# Read and parse input
num_test_cases = int(sys.stdin.readline())
patterns = []
for _ in range(num_test_cases):
    num_patterns = int(sys.stdin.readline())
    patterns = [sys.stdin.readline().strip() for _ in range(num_patterns)]
    
# Solve each test case and print the result
for i, pattern in enumerate(patterns):
    sys.stdout.write('Case #' + str(i+1) + ': ' + solve(pattern) + '\n')