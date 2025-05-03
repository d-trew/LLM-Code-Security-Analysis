import sys

def min_flips(pancakes):
    n = len(pancakes)
    flips = 0
    for i in range(n):
        if pancakes[i] == '-':
            break
        else:
            flips += 1
    return flips

def main():
    T = int(input())
    for case in range(1, T+1):
        pancakes = input()
        print("Case #%d: %d" % (case, min_flips(pancakes))

if __name__ == "__main__":
    main()