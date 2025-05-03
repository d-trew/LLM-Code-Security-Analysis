from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
cases = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < h) and (0 <= ny < w) and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
            dfs(nx, ny)

def solve():
    for i in range(h):
        for j in range(w):
            if not visited[i][j]:
                dfs(i, j)
                cnt = defaultdict(int)
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if (0 <= nx < h) and (0 <= ny < w) and grid[nx][ny] == grid[i][j]:
                        cnt[grid[nx][ny]] += 1
                ans = max(ans, min(cnt['B'], cnt['W']))
    return ans + 1 if ans != -1 else 0

for case in range(cases):
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    ans = -1
    print('Case #{}: {}'.format(case+1, solve()))