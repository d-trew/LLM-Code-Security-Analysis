from math import sqrt, pi

def visible_pillars(N, R):
    if N <= 1 or R > (10**6) // 2:
        return 0
    pillar_grid = [[False] * N for _ in range(N)]

    # Fill the grid with pillars
    for i in range(1, N):
        for j in range(1, N):
            pillar_grid[i][j] = True

    # Calculate the maximum distance from viewpoint that a pillar can be seen
    vp_x, vp_y = 0.5 * (N - 1), 0.5 * (N - 1)
    max_distance = sqrt((vp_x + R)**2 + (vp_y + R)**2)

    # Check visibility for each pillar
    visible = 0
    for i in range(1, N):
        for j in range(1, N):
            if pillar_grid[i][j]:
                distance = sqrt((vp_x - i)**2 + (vp_y - j)**2)
                if distance <= R and max_distance >= distance:
                    visible += 1
                    for k in range(max(0, i - int(max_distance)): min(i + int(max_distance) + 1, N)):
                        for l in range(max(0, j - int(max_distance)): min(j + int(max_distance) + 1, N)):
                            if (abs(k - i) <= R and abs(l - j) <= R):
                                pillar_grid[k][l] = False
    return visible + 1

T = int(input())
for t in range(1, T+1):
    N, R = map(int, input().split())
    print("Case #" + str(t) + ": " + str(visible_pillars(N, R)))