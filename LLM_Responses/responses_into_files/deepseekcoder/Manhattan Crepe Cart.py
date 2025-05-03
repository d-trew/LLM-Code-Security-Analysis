def solve():
    T = int(input())
    for t in range(1, T+1):
        P, Q = map(int, input().split())
        count = [[0]*(Q+2) for _ in range(Q+2)]
        direction = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for _ in range(P):
            Xi, Yi, Di = input().split()
            Xi, Yi = int(Xi)+1, int(Yi)+1
            dx, dy = direction[Di]
            x, y = Xi + dx, Yi + dy
            while 1 <= x <= Q + 1 and 1 <= y <= Q + 1:
                count[x][y] += 1
                x += dx
                y += dy
        max_count = 0
        for i in range(Q+2):
            for j in range(i, Q+2):
                if (max_count < min(i-1, j-1)):
                    max_count = count[i][j]
                    x, y = i - 1, j - 1
        print('Case #{}: {} {}'.format(t, x, y))
solve()