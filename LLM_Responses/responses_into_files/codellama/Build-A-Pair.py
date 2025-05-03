import sys

def solve(digits):
    """
    Given a list of digits, find the minimum absolute difference between two positive integers built from these digits.
    The order of the digits within each integer is not fixed, except that you cannot put a zero as the most significant digit in either integer.
    """
    # Sort the digits in descending order to make it easier to find pairs with minimal difference
    sorted_digits = sorted(digits, reverse=True)
    
    # Initialize variables to keep track of the current pair of integers and their minimum absolute difference
    curr_pair = [0, 0]
    min_diff = float('inf')
    
    # Iterate through the sorted digits
    for i in range(len(sorted_digits)):
        # If the current digit is not equal to the most significant digit of the previous pair, add it to the current pair
        if sorted_digits[i] != curr_pair[1]:
            curr_pair[0] = curr_pair[0] * 10 + sorted_digits[i]
        # Otherwise, add it to the next position in the current pair
        else:
            curr_pair[1] = curr_pair[1] * 10 + sorted_digits[i]
        
        # Calculate the absolute difference between the current pair of integers and update the minimum if necessary
        diff = abs(curr_pair[0] - curr_pair[1])
        if diff < min_diff:
            min_diff = diff
    
    return min_diff

# Read input
test_cases = int(input())
for t in range(test_cases):
    # Read the list of digits
    digits = list(map(int, input().strip()))
    
    # Find the minimum absolute difference between two positive integers built from these digits
    min_diff = solve(digits)
    
    # Print the result
    print("Case #{}: {}".format(t+1, min_diff))