Here's the Python code for the problem:


from collections import deque
def solve():
    T = int(input().strip())
    for t in range(T):
        R, C = map(int, input().split())
        grid = [list(input().strip()) for _ in range(R)]
        visited = [[0]*C for _ in range(R)]
        dx, dy = [-1,-1,1,1],[-1,1,-1,1]
        q = deque()
        print("Case #{}: ".format(t+1), end="")
        flag = 0
        for i in range(R):
            for j in range(C):
                if visited[i][j]: continue
                color = grid[i][j]
                q.append((i, j))
                while len(q) > 0:
                    x, y = q.popleft()
                    if visited[x][y]: continue
                    visited[x][y] = 1
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == color:
                            q.append((nx, ny))
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != color:
                        print("IMPOSSIBLE")
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 1:
                break
        if flag == 0:
            print("POSSIBLE")
            for i in range(R-1):
                for j in range(C-1):
                    if grid[i][j] == 'A' and grid[i+1][j+1] != 'B':
                        print('/')
                    elif grid[i][j] == 'B' and grid[i+1][j+1] != 'A':
                        print('\\')
                    else:
                        print('.')
                print()