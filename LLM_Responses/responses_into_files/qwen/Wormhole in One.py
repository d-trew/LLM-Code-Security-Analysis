def max_distinct_holes(N, holes):
    from itertools import combinations

    def is_reachable(hole1, hole2):
        return abs(hole1[0] - hole2[0]) + abs(hole1[1] - hole2[1])

    def dfs(start, visited, path):
        if start in visited:
            return len(visited)
        visited.add(start)
        max_holes = 1
        for hole in holes:
            if hole not in visited and is_reachable(start, hole) == 0:
                max_holes = max(max_holes, dfs(hole, visited.copy(), path + [hole]))
        return max_holes

    max_touches = 1
    for start in range(N):
        visited = set()
        max_touches = max(max_touches, dfs(start, visited, [holes[start]]))

    for wormholes in combinations(holes, 2):
        visited = set(wormholes)
        hole1, hole2 = wormholes
        max_holes = dfs(hole1, visited, [hole1])
        max_holes = max(max_holes, dfs(hole2, visited, [hole2]))
        max_touches = max(max_touches, max_holes)

    return max_touches

T = int(input())
results = []
for i in range(T):
    N = int(input())
    holes = [tuple(map(int, input().split())) for _ in range(N)]
    results.append(max_distinct_holes(N, holes))

for i, result in enumerate(results):
    print(f"Case #{i+1}: {result}")