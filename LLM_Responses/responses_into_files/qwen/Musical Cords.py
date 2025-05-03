import math
for _ in range(int(input())):
    n = int(input())
    r = float(input())
    k = int(input())
    Ls = [0] * n
    for i in range(n):
        di, Li = map(int, input().split())
        Ls[i] = Li
    cords = []
    for i in range(n):
        for j in range(i+1, n):
            d = abs((j-i) * 360 / (n-1)) % 360
            length = r + Ls[i] + Ls[j] - 2 * math.cos(math.radians(d)) * r
            cords.append(length)
    cords.sort(reverse=True)
    print(f"Case # {_+1}: {' '.join(map(str, cords[:k]))}")