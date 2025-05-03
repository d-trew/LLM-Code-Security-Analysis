from itertools import permutations

def min_diff(digits):
    # Generate all possible permutations of the digits
    perms = [''.join(p) for p in permutations(digits)]
    
    min_difference = float('inf')
    for perm in perms:
        # Split the permutation into two numbers without leading zeros
        num1, num2 = int(perm[:-1]), int(perm[-1])
        
        # Skip if any of the numbers are 0 or negative
        if num1 <= 0 or num2 <= 0:
            continue
            
        # Update min_difference if necessary
        min_difference = min(min_difference, abs(num1 - num2))
    
    return min_difference

T = int(input())
for t in range(1, T+1):
    digits = input()
    print('Case #{}: {}'.format(t, min_diff(digits)))