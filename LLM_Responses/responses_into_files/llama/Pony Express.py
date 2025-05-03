import heapq

def pony_express(N, E, D):
    horse_speeds = [[0] * (N+1) for _ in range(N+1)]
    horse_distances = [[float('inf')] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        horse_speeds[i][i] = 1
        horse_distances[i][i] = 0

    for i in range(1, N+1):
        for j in range(i+1, N+2):
            if D[i-1][j-i-1] != -1:
                horse_speeds[i][j] = min(horse_speeds[i][j], horse_speeds[i][i] + E[i-1])
                horse_distances[i][j] = min(horse_distances[i][j], horse_distances[i][i] + D[i-1][j-i-1])

    Q = 1
    U = 1
    V = N

    total_time = horse_distances[U][V]

    return Case #{}: {:.6f}\n'.format(Q, total_time)

T = int(input())
for _ in range(T):
    N = int(input())
    E = [int(x) for x in input().split()]
    D = [[int(x) for x in input().split()] for _ in range(N)]
    print(pony_express(N, E, D))