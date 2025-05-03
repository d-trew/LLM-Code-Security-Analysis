import math
from itertools import combinations

def distance(i, j):
    return round((2 * math.pi * R) / N * abs(j - i), 9)

T = int(input())
for t in range(1, T + 1):
    N, R, K = map(int, input().split())
    D = [tuple(map(int, input().split())) for _ in range(N)]
    D.sort(key=lambda x: x[0])
    cords = []
    for i in range(N):
        for j in range(i + 1, N):
            if abs(D[i][0] - D[j][0]) % (360 * 10**9) < 5:
                cord_length = distance(D[i][0], D[j][0]) + D[i][1] + D[j][1]
                cords.append((cord_length, i, j))
    cords.sort(reverse=True)
    print("Case #{}: {}".format(t), end="")
    for cord in cords[:K]:
        print(" {:.9f}".format(cord[0]), end="")
    print()