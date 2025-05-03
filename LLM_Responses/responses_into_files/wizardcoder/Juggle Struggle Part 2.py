import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline()
    T = int(input())
    for t in range(1, T + 1):
        N = int(sys.stdin.readline().strip())
        jugglers = []
        pairs = defaultdict(set)
        for i in range(N):
            x, y, x2, y2 = map(int, sys.stdin.readline().split())
            jugglers.append((x, y))
            jugglers.append((x2, y2))
            pairs[i].add((x, y))
            pairs[N + i].add((x2, y2))
        for i in range(N):
            for j in range(i + 1, N):
                if not is_collinear(jugglers[i], jugglers[j]):
                    pairs[i].add(j)
                    pairs[j].add(i)
        result = set()
        for i in range(N):
            if len(pairs[i]) < N - 1:
                result.add(i + 1)
        print("Case #{}:".format(t), "MAGNIFICENT" if not result else sorted(result))

def is_collinear(j1, j2):
    x1, y1 = j1
    x2, y2 = j2
    return (x1 - x2) * (y1 - y2) == 0

main()