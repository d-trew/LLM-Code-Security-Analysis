def solve():
    C, R, M = map(int, input().split())
    grid = [list(input()) for _ in range(R)]

    soldiers = []
    turrets = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                soldiers.append((r, c))
            elif grid[r][c] == 'T':
                turrets.append((r, c))

    num_soldiers = len(soldiers)
    num_turrets = len(turrets)

    #This is a simplified solution that doesn't guarantee finding the optimal solution for all cases, especially larger ones.  A more sophisticated approach (e.g., using constraint programming or a more advanced search algorithm) would be needed for optimal results in all scenarios exceeding small problem sizes.

    destroyed_turrets = []
    soldier_turret_pairs = []

    for i in range(num_soldiers):
        min_dist = float('inf')
        closest_turret = -1
        for j in range(num_turrets):
            if j not in [t[1] for t in destroyed_turrets]:
                dist = abs(soldiers[i][0] - turrets[j][0]) + abs(soldiers[i][1] - turrets[j][1])
                if dist <= M and dist < min_dist:
                    min_dist = dist
                    closest_turret = j

        if closest_turret != -1:
            destroyed_turrets.append((i, closest_turret))

    return len(destroyed_turrets), destroyed_turrets


T = int(input())
for i in range(1, T + 1):
    max_destroyed, pairs = solve()
    print(f"Case #{i}: {max_destroyed}")
    for soldier_id, turret_id in pairs:
        print(soldier_id + 1, turret_id + 1)