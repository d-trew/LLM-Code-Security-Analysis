import sys

def longest_straight(dice):
    # Find the longest straight in the list of dice
    longest = []
    for die in dice:
        straight = sorted(set(die))
        if len(straight) > len(longest):
            longest = straight
    return longest

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        dice = []
        for i in range(n):
            die = list(map(int, input().split()))
            dice.append(die)
        longest = longest_straight(dice)
        print("Case #{}".format(_+1), len(longest))