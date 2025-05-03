import sys

# Read number of test cases from standard input
t = int(input())

# Process each test case
for i in range(t):
    # Read A, B, and N from standard input
    a, b, n = map(int, input().split())

    # Initialize the guess to the middle of the range
    guess = (a + b) // 2

    # Check if the guess is correct
    if guess == b:
        print("CORRECT")
        continue

    # Otherwise, check if the guess is too small or too large
    if guess < b:
        print("TOO_SMALL")
    else:
        print("TOO_BIG")

    # Update the guess based on the response from the judge
    if sys.stdin.readline().strip() == "TOO_SMALL":
        guess = (guess + a) // 2
    elif sys.stdin.readline().strip() == "TOO_BIG":
        guess = (guess + b) // 2

# If the test case is solved within N tries, print CORRECT and continue to the next test case
if sys.stdin.readline().strip() == "CORRECT":
    print("CORRECT")
else:
    # If the test case is not solved within N tries, print WRONG_ANSWER and stop reading from standard input
    if sys.stdin.readline().strip() == "WRONG_ANSWER":
        print("WRONG_ANSWER")