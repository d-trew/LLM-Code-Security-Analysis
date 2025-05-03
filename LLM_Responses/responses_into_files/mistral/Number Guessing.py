import sys
from itertools import islice

def get_input():
    return sys.stdin.readline().strip()

def main():
    t = int(get_input())
    for _ in range(t):
        a, b, n = map(int, get_input().split())
        guesses = [(a + b) // 2]
        while n > 1:
            response = get_input()
            if response == "CORRECT":
                print(guesses[-1])
                break
            elif response == "TOO_SMALL":
                guesses += [guesses[-1] + (b - a) // 2 + 1]
            elif response == "TOO_BIG":
                guesses += [guesses[-1] - ((b - a + 1) * 2) // 3]
            n -= 1
        else:
            print("WRONG_ANSWER")

if __name__ == "__main__":
    main()