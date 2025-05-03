import math

def count_visible_pillars(n, r):
    # Calculate the number of visible pillars
    total = 0
    for i in range(1, n+1):
        if (i * r / 2) < 1:
            total += n - i + 1
        else:
            total += math.floor((n - i + 1) * math.pi * (i * r / 2))
    return total

def main():
    # Read input
    t = int(input())
    for case in range(1, t+1):
        n, r = map(int, input().split())
        print("Case #{}: {}".format(case, count_visible_pillars(n, r)))

if __name__ == "__main__":
    main()