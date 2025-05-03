from math import inf
import sys
input = sys.stdin.read().splitlines()
T = int(input[0])
for _ in range(T):
    N, D = map(int, input[1].split())
    repair_centers = [list(map(int, input[i+2].split())) for i in range(N)]
    red_points = set()
    blue_points = set()
    for x, y in repair_centers:
        for dx in range(-D, D+1):
            for dy in range(-D, D+1):
                if (dx or dy) and abs(x - x + dx) + abs(y - y + dy) <= D:
                    red_points.add((x + dx, y + dy))
    for i, (x, y) in enumerate(repair_centers):
        info = set()
        for dx in range(-D, D+1):
            for dy in range(-D, D+1):
                if abs(x - x + dx) + abs(y - y + dy) <= D:
                    info.add((dx, dy))
        blue_points.update({(x + dx, y + dy) for dx, dy in info if (x + dx, y + dy) not in repair_centers})
    red_area = sum((D - x + 1) * (2 * D - y + 1) for x, y in red_points)
    blue_area = sum((D - x + 1) * (2 * D - y + 1) for x, y in blue_points)
    print(f"Case #{_ + 1}: {red_area / (red_area + blue_area)}")