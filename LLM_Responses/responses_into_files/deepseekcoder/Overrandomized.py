from collections import defaultdict
import random
import string

def solve(records):
    U = len(records[0]) - 1
    digit_map = list(string.ascii_uppercase)
    random.shuffle(digit_map)
    
    # Create a dictionary to map each character in the digit string to its corresponding value
    char_to_value = {char: i for i, char in enumerate(digit_map)}
    
    # Count the frequency of each character in all records
    freqs = defaultdict(int)
    for record in records:
        for char in record[1]:
            freqs[char] += 1
            
    # Sort characters by their frequencies and shuffle them if they have the same frequency
    chars_ordered = sorted(freqs.items(), key=lambda x: (-x[1], random.random()))
    
    # Create a mapping from digit string to value
    value_to_char = {i: char for i, (char, _) in enumerate(chars_ordered)}
    
    # Reconstruct the original digit string
    digit_string = ''.join([value_to_char[i] for i in range(10)])
    
    return digit_string

T = int(input())
for tc in range(1, T+1):
    U = int(input().split()[-1])
    records = [input().split() for _ in range(U)]
    print('Case #{}: {}'.format(tc, solve(records)))