import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def solve():
    N, S = map(int, input().split())
    asteroids = []
    for _ in range(N):
        asteroids.append(list(map(int, input().split())))

    best_max_dist = float('inf')

    q = [(0, [], 0)]  # (current_asteroid, path, max_dist_so_far)

    while q:
        curr_asteroid, path, max_dist = q.pop(0)

        if curr_asteroid == 1:
            best_max_dist = min(best_max_dist, max_dist)
            continue

        for next_asteroid in range(N):
            if next_asteroid != curr_asteroid:
                
                time_elapsed = 0 if not path else path[-1][1]

                
                curr_pos = [asteroids[curr_asteroid][i] + asteroids[curr_asteroid][i+3] * time_elapsed for i in range(3)]
                next_pos = [asteroids[next_asteroid][i] + asteroids[next_asteroid][i+3] * time_elapsed for i in range(3)]

                jump_dist = dist(curr_pos, next_pos)

                
                q.append((next_asteroid, path + [(curr_asteroid, time_elapsed)], max(max_dist, jump_dist)))

    return best_max_dist


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")