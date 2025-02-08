def solve():
    R, C, S = map(int, input().split())
    stations = []
    for _ in range(S):
        stations.append(list(map(int, input().split())))

    grid = [[0 for _ in range(C)] for _ in range(R)]
    patrol_areas = [[] for _ in range(S)]

    for i in range(S):
        r, c, d = stations[i]
        r -= 1
        c -= 1
        for x in range(max(0, r - d), min(R, r + d + 1)):
            for y in range(max(0, c - d), min(C, c + d + 1)):
                if max(abs(x - r), abs(y - c)) <= d:
                    patrol_areas[i].append((x,y))
                    grid[x][y] = i + 1

    
    assignable = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                can_patrol = False
                for i in range(S):
                    if (r,c) in patrol_areas[i]:
                        can_patrol = True
                        break
                if can_patrol:
                    assignable.append((r,c))

    assignments = [0] * S
    
    for r,c in assignable:
        best_station = -1
        min_assignments = float('inf')
        for i in range(S):
            if (r,c) in patrol_areas[i]:
                if assignments[i] < min_assignments:
                    min_assignments = assignments[i]
                    best_station = i
        assignments[best_station] +=1

    return max(assignments) - min(assignments)


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")