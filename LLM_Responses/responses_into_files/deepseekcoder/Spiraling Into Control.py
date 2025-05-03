from collections import deque

def bfs(start, end):
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for x_next, y_next in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= x_next < N and 0 <= y_next < N:
                queue.append(path + [(x_next, y_next)])
                
def find_shortcuts(n, k):
    N = n * n
    start = (0, 0)
    end = (N-1, N-1)
    path = bfs(start, end)
    if len(path)-1 > k:
        return "IMPOSSIBLE"
    shortcuts = []
    for i in range(len(path)-2):
        x1, y1 = path[i]
        x2, y2 = path[i+1]
        if abs(x1-x2) + abs(y1-y2) == 1:
            shortcuts.append((n*(x1+1)-y1, n*(x2+1)-y2))
    return len(shortcuts), shortcuts[::-1][:k]

T = int(input().strip())
for t in range(T):
    N, K = map(int, input().split())
    result = find_shortcuts(N, K)
    if result == "IMPOSSIBLE":
        print("Case #{}: {}".format(t+1, result))
    else:
        n, shortcuts = result
        print("Case #{}: {}".format(t+1, n))
        for shortcut in shortcuts[::-1]:
            print(*shortcut)