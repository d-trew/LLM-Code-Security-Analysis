import sys
from collections import namedtuple

TestCase = namedtuple("TestCase", ["A", "B", "N"])

def main():
    T = int(input())  # Read number of test cases
    for i in range(T):
        A, B, N = map(int, input().split())  # Read the three integers for each test case
        guessed_range = B - A + 1
        if guessed_range > 30:
            print("WRONG_ANSWER")
            sys.exit()
        
        P = (A + B) // 2  # Guess the middle of the range as initial guess
        for _ in range(N):
            print(P)  # Output your guess to standard output
            response = input().strip()  # Read judge's response from stdin
            
            if response == "CORRECT":
                break
            elif response == "TOO_SMALL":
                P = (A + P) // 2
            else:  # response == "TOO_BIG"
                P = (P + B) // 2
        else:
            print("WRONG_ANSWER")  # If not solved after N tries, output WRONG_ANSWER and exit with error code 1
        
    sys.exit(0)
    
if __name__ == "__main__":
    main()