from collections import deque

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def get_picture(x, y, path):
    q = deque([(x, y, 0)])
    visited = set()
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    while q:
        x, y, minutes = q.popleft()
        if (x, y) == (path[0][0], path[0][1]): # If the starting point of the tour is reached
            return minutes

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(path) and 0 <= ny < len(path[0]) and (nx, ny) not in visited:
                q.append((nx, ny, minutes + 1))
                visited.add((nx, ny))

    return float('inf') # If no picture can be taken

T = int(input())
for _ in range(T):
    x, y, path = map(int, input().split())
    path_str = input()

    minutes = get_picture(0, 0, [[x + i, y + j] for i, j in enumerate(zip(range(x), path_str)) if j == 'E') + \
                          [[i + x, j + y] for i, j in enumerate(zip(range(y), reversed(path_str[::-1])) if j == 'N']])
    print(f'Case #{_+ 1}: {minutes} (IMPOSSIBLE if minutes is infinite)')


This Python code reads the input, calculates the minimum number of minutes required to get a picture with Peppurr using Breadth-First Search and stores the tour path in a list of lists. The `get_picture()` function takes as input the current position (x, y), the tour path, and returns the smallest number of minutes needed to take a picture with Peppurr or float('inf') if no picture can be taken.