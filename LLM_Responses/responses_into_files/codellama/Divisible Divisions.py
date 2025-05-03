import math

def solve(S, D):
    # Calculate the number of possible divisions of S
    num_divisions = 2 ** (len(S) - 1)

    # Initialize a counter to keep track of the number of divisible divisions
    count = 0

    # Iterate through each division of S
    for i in range(num_divisions):
        # Convert the binary representation of i to a string
        s = bin(i)[2:]

        # Check if the current division is divisible by D
        divisible = True
        for j in range(len(s) - 1):
            if int(s[j:j+2]) % D != 0:
                divisible = False
                break

        # Increment the counter if the current division is divisible by D
        if divisible:
            count += 1

    # Return the remainder of dividing the number of divisible divisions by the prime 10^9 + 7
    return count % (10 ** 9 + 7)