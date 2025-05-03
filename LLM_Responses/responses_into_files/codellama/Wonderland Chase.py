import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    J, C, A, Q = map(int, input().split())
    graph = [[] for _ in range(J+1)]
    for _ in range(C):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    if A == Q:
        print("Case #%d: SAFE" % (t+1))
    else:
        dp = [[float('inf') for _ in range(J+1)] for _ in range(2)]
        dp[0][A] = 0
        for i in range(1, 10**9):
            if dp[i%2][Q] < float('inf'):
                break
            for j in range(1, J+1):
                if dp[(i-1)%2][j] == float('inf'):
                    continue
                for k in graph[j]:
                    dp[i%2][k] = min(dp[i%2][k], dp[(i-1)%2][j] + 1)
        if dp[i%2][Q] < float('inf'):
            print("Case #%d: %d" % (t+1, i*2))
        else:
            print("Case #%d: SAFE" % (t+1))