import itertools
from collections import defaultdict

def possible_maze(R, C, pairs):
    if not pairs:
        return True

    lovers = defaultdict(set)
    for i in pairs:
        lovers[i].add(pairs[(pairs.index(i)+1) % len(pairs)])

    # Check if all lovers are connected
    graph = build_graph(R, C, lovers)
    return all([is_reachable(graph, s, t) for s, t in lovers.items()])

def build_graph(R, C, lovers):
    grid = [['.' for _ in range(C)] for _ in range(R)]
    for i, j in itertools.product(range(R), range(C)):
        if (i, j) == (0, 0) or (i, j) == (R-1, C-1):
            continue
        x, y = i, j
        wall = '/' if x % 2 == y % 2 else '\\'
        grid[x][y] = wall

        # Connect to neighbors
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < R and 0 < ny < C:
                grid[nx][ny] = wall[::-1]
    return grid

def is_reachable(grid, sx, sy):
    visited = set()
    queue = [(sx, sy)]
    while queue:
        x, y = queue.pop(0)
        if (x, y) == (len(grid)-1, len(grid[0])-1):
            return True
        visited.add((x, y))
        for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            nx, ny = x + dx, y + dy
            if 0 < nx < len(grid) and 0 < ny < len(grid[0]) and grid[nx][ny] != grid[x][y] and (nx, ny) not in visited:
                queue.append((nx, ny))
    return False

def solve():
    T = int(input().strip())
    for _ in range(T):
        R, C = map(int, input().split())
        pairs = list(map(int, input().split()))
        if possible_maze(R, C, pairs):
            maze = build_graph(R, C, {p: [pairs[(p+1) % len(pairs)] for p in pairs})
            print(f"Case #{_+1}:")
            for row in maze:
                print(''.join(row))
        else:
            print(f"Case #{_+1}: IMPOSSIBLE")

solve()


This code takes input as test cases, where each test case consists of the number of rows and columns, followed by a list of pairs of lovers. It checks if it's possible to build a maze that connects all the lovers, and if so, it prints the maze. If it's impossible, it prints "IMPOSSIBLE". The code uses a graph data structure to represent the hedge maze and a breadth-first search algorithm to check if all lovers are reachable from each other.