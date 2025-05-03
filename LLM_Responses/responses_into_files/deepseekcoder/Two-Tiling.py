Here's a Python program based on your description:


from collections import deque
import sys
input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0:
                if board[nx][ny] == '@':
                    q.append((nx, ny))
                    visited[nx][ny] = 1

def solve():
    for i in range(h):
        for j in range(w):
            if board[i][j] == '.' or visited[i][j]:
                continue
            bfs(i, j)
            cnt += 1

t = int(input())
for _ in range(t):
    h, w = 4, 3
    board = [['.']*w for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h+1):
        line = input().rstrip()
        if not line: break
        board[i%4][:] = list(line[:3])
    solve()
    print('Case #{}: {}'.format(_+1, 'POSSIBLE' if cnt == 1 else 'IMPOSSIBLE'))


This program uses a Breadth-First Search (BFS) algorithm to find connected components in the board. It assumes that an empty cell is represented by '.', and a filled cell is represented by '@'. If there are more than one connected component, it means there's no solution for the puzzle.