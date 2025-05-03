import sys
from itertools import combinations_with_replacement
from collections import defaultdict

def longest_straight(dice):
    sides = {side for die, side in dice}
    max_length = 0
    for i in range(1, len(sides) - max(dice)+1):
        combos = combinations_with_replacement([die for die, _ in dice], i)
        for combo in combos:
            straight = defaultdict(int)
            for die, side in dice:
                if die in combo and side < 10**6:
                    straight[side] += 1
            if max_length < len(straight):
                max_length = max(max_length, sum(count >= i for count in straight.values())+1)
        if max_length == len(dice):
            break
    return max_length

def main():
    T = int(input())
    cases = [list(map(int, input().split())) for _ in range(T)]
    for i, (N, *S) in enumerate(cases, 1):
        dice = [(i, s) for i, s in enumerate(S, 1)]
        print(f"Case #{i}: {longest_straight(dice)}")

if __name__ == "__main__":
    main()