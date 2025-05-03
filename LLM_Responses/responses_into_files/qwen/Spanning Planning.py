T = int(input())
for t in range(1, T+1):
    K = int(input())
    N = 3 + K // 2 if K % 2 == 0 else 3 + (K - 1) // 2
    graph = [['0'] * N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if (i+j) <= N:
                graph[i][j] = '1'
                graph[j][i] = '1'
    print(f"Case #{t}: {N}")
    for row in graph:
        print(''.join(row))