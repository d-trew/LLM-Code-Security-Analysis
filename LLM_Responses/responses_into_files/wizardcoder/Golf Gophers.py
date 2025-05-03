import sys
from collections import defaultdict

def main():
    T, N, M = map(int, input().split())
    gopher_counts = defaultdict(int)

    for i in range(T):
        for j in range(N + 1):
            windmill_blades = list(map(int, input().split()))
            for blade in windmill_blades:
                gopher_counts[blade] += 1
        print(*gopher_counts.values())

if __name__ == "__main__":
    main()