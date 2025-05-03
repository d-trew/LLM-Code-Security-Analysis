import sys

def count_googlements(googlement):
    L = len(googlement)
    ones = googlement.count('1')
    twos = googlement.count('2')
    threes = googlement.count('3')
    fours = googlement.count('4')
    if L == 1:
        return 1
    elif L == 2:
        return ones + twos
    else:
        return (ones * count_googlements(twos)) + (twos * count_googlements(threes)) + (threes * count_googlements(fours))

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        googlement = input()
        print("Case #{}".format(t), count_googlements(googlement))