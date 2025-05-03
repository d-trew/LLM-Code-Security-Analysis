import sys

def solve(cards):
    """
    Given a list of cards, return the maximum possible final value as an irreducible fraction with a positive denominator.
    """
    # Initialize the starting value and the number of cards
    start_value = 0
    num_cards = len(cards)

    # Initialize the denominator and the numerator for the final result
    denom = 1
    num = 0

    # Iterate through each card in the list
    for i in range(num_cards):
        op, operand = cards[i]

        # Apply the operation to the starting value
        if op == '+':
            start_value += operand
        elif op == '-':
            start_value -= operand
        elif op == '*':
            start_value *= operand
        else:  # op == '/'
            start_value //= operand

    # Return the final result as an irreducible fraction with a positive denominator
    return gcd(start_value, denom), start_value // gcd(start_value, denom)

def gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Read input
num_cases = int(input())
cases = []
for i in range(num_cases):
    start_value, num_cards = map(int, input().split())
    cards = []
    for _ in range(num_cards):
        op, operand = input().split()
        operand = int(operand)
        cards.append((op, operand))
    cases.append((start_value, num_cards, cards))

# Print output
for case in cases:
    start_value, num_cards, cards = case
    result = solve(cards)
    print("Case #{}: {}/{}".format(i + 1, result[0], result[1]))