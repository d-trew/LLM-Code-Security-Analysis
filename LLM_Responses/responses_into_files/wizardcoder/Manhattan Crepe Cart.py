import sys
sys.setrecursionlimit(10**6)
T = int(input())
for t in range(1, T+1):
    P, Q = map(int, input().split())
    people_movement = []
    for i in range(P):
        x, y, direction = map(str, input().split())
        x, y = int(x), int(y)
        if direction == "N":
            people_movement.append((x+1, y))
        elif direction == "S":
            people_movement.append((x-1, y))
        elif direction == "E":
            people_movement.append((x, y+1) if x < Q else (0, 0))
        elif direction == "W":
            people_movement.append((x, y-1) if y > 0 else (Q, Q))
    min_x = min(people_movement, key=lambda p: (p[0], -p[1]) if p[0] >= 0 and p[1] >= 0 else (float("inf"), float("inf")))[0]
    min_y = min(filter(lambda p: p[0] == min_x, people_movement, key=lambda p: (-p[1]) if p[1] >= 0 else float("inf"))[1]
    print("Case #{}: {} {}".format(t, min_x, min_y))