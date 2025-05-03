import sys
from collections import defaultdict

def solve():
    for _ in range(int(sys.stdin.readline())):
        k, c, s = map(int, sys.stdin.readline().split())
        if s > k or s * (c - 1) >= k:
            print("IMPOSSIBLE")
        else:
            tiles = [0] * k
            for _ in range(c):
                tiles = [tiles[i + j] + tiles[i] for i, j in enumerate([-1, 1])]
            tiles[-s:] = [1] * s
            tiles = list(set(tiles))
            print("Case #{}: {}".format(sys.stdin.readline().strip(), sorted(tiles)))

solve()