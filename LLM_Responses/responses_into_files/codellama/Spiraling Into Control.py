import math

def dantes_house(n, k):
    if n % 2 == 0:
        return "IMPOSSIBLE"
    if k >= n * n - 1:
        return str(n * n - 1)
    else:
        return "IMPOSSIBLE"

def main():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print("Case #" + str(i+1) + ":", dantes_house(n, k))

if __name__ == "__main__":
    main()