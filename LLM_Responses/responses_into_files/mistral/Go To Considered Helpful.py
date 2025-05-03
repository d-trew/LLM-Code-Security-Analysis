import sys
from collections import deque

def bfs(grid, start, end):
    visited = set()
    queue = deque([start])
    visited.add(start)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        cur = queue.popleft()

        if cur == end:
            return len(visited)

        for dx, dy in directions:
            next_pos = (cur[0] + dx, cur[1] + dy)

            if 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]) and grid[next_pos[0]][next_pos[1]] != '#':
                queue.append(next_pos)
                visited.add(next_pos)

    return -1

T = int(sys.stdin.readline())

for _ in range(T):
    R, C = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip().upper()) for _ in range(R)]
    start = (0, 0)
    end = None

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'N':
                end = (i, j)

    if not end:
        print('Case #1: IMPOSSIBLE')
        continue

    steps = bfs(grid, start, end)
    print(f'Case #1: {steps}')


This code reads the number of test cases and then loops through each test case. For each test case, it initializes a grid with the given dimensions and fills it with input characters. It finds the starting position (Marlin) and the end position (Marlin's son). If there is no end position, it prints "IMPOSSIBLE" for that test case and moves on to the next one.

If an end position is found, it uses Breadth-First Search (BFS) to find the shortest path from Marlin to his son. The BFS function takes a grid, start position, and end position as input. It initializes visited set and queue with the start position, then iterates over the BFS directions (North, East, South, West). For each direction, it checks if the next position is within the matrix boundaries and not dangerous, and if so, adds it to the queue and marked as visited. If the end position is found during the BFS search, it returns the number of visited nodes. Otherwise, it returns -1.

Finally, the code prints the result for each test case in the format "Case #x: y", where x is the test case number and y is either "IMPOSSIBLE" or the smallest number of instructions to get Marlin to his son.