import math

def solve():
    N, R, K = map(int, input().split())
    points = []
    for _ in range(N):
        D, L = map(int, input().split())
        points.append((D, L))

    cord_lengths = []
    for i in range(N):
        for j in range(i + 1, N):
            d1, l1 = points[i]
            d2, l2 = points[j]
            
            angle_diff = abs(d1 - d2)
            angle_rad = math.radians(min(angle_diff, 360 * 10**9 - angle_diff) * 10**(-9))
            distance = 2 * R * math.sin(angle_rad / 2)
            cord_lengths.append(l1 + l2 + distance)

    cord_lengths.sort(reverse=True)
    return " ".join(map(str, cord_lengths[:K]))

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")