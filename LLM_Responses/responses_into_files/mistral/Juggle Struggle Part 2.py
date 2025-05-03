import sys
from itertools import combinations

def solve(cases):
    for i, test_case in enumerate(cases):
        n = test_case[0]
        pairs = sorted([list(map(tuple, pair)) for pair in combinations(test_case[1:], 2)])
        intersections = []
        for i, (x1, y1), (x2, y2) in enumerate(pairs):
            for j, (x3, y3), (x4, y4) in pairs[i + 1:]:
                if ((x1 == x3 and y1 == y3 and x2 == x4 and y2 == y4) or
                        (x1 - x3) * (y2 - y4) - (x2 - x4) * (y1 - y3)):
                    intersections.append(i + 1)

        if len(intersections) > 25:
            print("Case #{}: Magnificent".format(i + 1))
        else:
            print("Case #{}: {}".format(i + 1, ", ".join(str(x) for x in sorted(set(intersections)))))

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        data = []
        for _ in range(N):
            x, y, x_, y_ = map(int, sys.stdin.readline().split())
            data.append((x, y, x_, y_))
        solve([[data]])