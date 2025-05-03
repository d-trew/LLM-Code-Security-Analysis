import sys
from collections import defaultdict

def use_well(day):
    # Use the well of knowledge to get the number of rings at day 'day'
    # Return the result modulo 263
    pass

def solve():
    T, W = map(int, input().split())

    for _ in range(T):
        R = [0] * 7  # Initialize array to store number of rings for each type
        guesses = []

        for _ in range(W + 1):
            guess = input()
            if guess == '-1':
                break
            else:
                guesses.append(guess.split())

        # Make initial guess about the number of rings at day 0
        R[0] = len(guesses) // W + 1
        for i in range(1, 7):
            R[i] = R[0]

        for _ in range(W):
            # Use the well to check our guess and update it if necessary
            rings_at_day_500 = use_well(500) % 263
            diff = rings_at_day_500 - sum([r * (i + 1) for i, r in enumerate(R)])
            R[6 - (diff - 1) // 6] += 1 if diff < 0 else R[6 - (diff + 1) // 6] -= 1

        print(*R)

solve()


This code reads the number of test cases and the number of times we can use the well of knowledge per test case. It then processes each test case by making a guess about the number of rings at day 0, using the well of knowledge to check our guess and update it if necessary up to W times. Finally, it prints the number of rings for each type.