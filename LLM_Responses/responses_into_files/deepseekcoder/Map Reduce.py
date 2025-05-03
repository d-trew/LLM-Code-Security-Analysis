from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dirs = ['u', 'l', 'd', 'r']

def bfs(start):
    q = deque()
    visited = [[[False]*c for _ in range(r)] for __ in range(2)]
    x, y, z, d = start
    q.append((x, y, z, d))
    visited[z][y][x] = True
    
    while q:
        x, y, z, d = q.popleft()
        
        if (x, y) == finish:
            return d, [''.join(path[1:]) for path in dirs[:d+1]]
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and not visited[z][ny][nx]:
                if maze[ny][nx] == '.':
                    q.append((nx, ny, z, d+1))
                    visited[z][ny][nx] = True
                elif maze[ny][nx] == '#' and z == 0:
                    q.append((nx, ny, 1, d+1))
                    visited[1][ny][nx] = True
    return -1, []

t = int(input())
for tc in range(1, t+1):
    r, c, d = map(int, input().split())
    maze = [list(input().strip()) for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'S':
                start = (j, i, 0, 0)
            elif maze[i][j] == 'F':
                finish = (j, i)
    
    length, paths = bfs(start)
    if length != -1 and length <= d:
        print(f'Case #{tc}: POSSIBLE')
        for path in paths[:d]:
            print(path)
    else:
        print(f'Case #{tc}: IMPOSSIBLE')