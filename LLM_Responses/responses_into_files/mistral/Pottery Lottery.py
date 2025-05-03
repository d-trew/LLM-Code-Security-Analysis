import sys
from collections import defaultdict

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        days, actions = list(map(int, sys.stdin.readline().split()))
        vases = defaultdict(int)
        for day in range(days):
            if day < 99:
                action = int(sys.stdin.readline())
                vases[action] += 1
            elif day == 99:
                pass
            else:
                vase = int(sys.stdin.readline())
                vases[vase] += 1
        winning_vase = max(vases, key=vases.get)
        if winning_vase != 100:
            sys.stdout.write("-1\n")
            continue
        for vase in vases:
            if vases[vase] > 1 and vase != 100:
                sys.stdout.write("-1\n")
                break
        else:
            sys.stdout.write(f"{winning_vase}\n")

if __name__ == "__main__":
    main()


This Python code reads the number of test cases, then iterates through each test case by reading the number of days and actions for each day from the standard input. It uses a dictionary (`defaultdict`) to store the count of tokens in each vase. For days 1-99, it simulates the action of the i-th player by incrementing the count of the corresponding vase. On day 100, it simply reads the number of the vase where the token is inserted. After processing all the days for a test case, it checks if the winning vase (i.e., the vase with the highest count) is player 100 and if there are no other vases with more than one token for the same player. If either condition is not met, it outputs -1 and moves on to the next test case. Otherwise, it outputs the winning vase number.