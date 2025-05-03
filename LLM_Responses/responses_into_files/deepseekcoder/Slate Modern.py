from heapq import *
import sys
input = sys.stdin.readline
MOD = 10**9+7
INF = float('inf')
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solve():
    T = int(input())
    for t in range(T):
        R, C, N, D = map(int, input().split())
        grid = [[INF]*(C+2) for _ in range(R+2)]
        painted = []
        for _ in range(N):
            r, c, b = map(int, input().split())
            grid[r][c] = b
            painted.append((b, r, c))
        
        dp = [0]*(R*C+1)
        heap = []
        for i in range(1, R+1):
            for j in range(1, C+1):
                if grid[i][j] != INF:
                    heappush(heap, (grid[i][j], -i, -j))
        
        res = 0
        while heap:
            b, r, c = (-heappop(heap)[1:] for _ in range(3))
            idx = (r-1)*C + (c-1)
            dp[idx] = max(dp[idx], b+max((dp[(i-1)*C+j-1] if 1<=i<R and 1<=j<C else -INF) for i, j in zip([r-1, r, r, r+1], [c, c-1, c+1, c]))
            res = max(res, dp[idx])
        
        print('Case #%d: %d' % (t+1, res%MOD))
solve()