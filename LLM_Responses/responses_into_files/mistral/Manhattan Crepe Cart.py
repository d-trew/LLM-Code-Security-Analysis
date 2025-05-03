import sys
from collections import defaultdict
input = sys.stdin.readline

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_crepe_cart(people):
    directions = defaultdict(int)
    for x, y, d in people:
        directions[(x, y)] += 1
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and (nx, ny) not in directions:
                directions[(nx, ny)] -= 1
    max_count = max(directions.values())
    cart_locations = [k for k, v in directions.items() if v == max_count]
    return min(cart_locations, key=lambda x: (x[0], -x[1]))

T = int(input().strip())
for _ in range(T):
    P, Q = map(int, input().split())
    people = []
    for _ in range(P):
        x, y, d = map(int, input().split()), input().strip()[0]
        people.append((x, y, (1 if d == 'N' else -1) * y, (1 if d == 'E' else -1) * x))
    print('Case #{}: {}'.format(_ + 1, find_crepe_cart(people)))