import sys
from collections import defaultdict
input = sys.stdin.readline

def solve(holes):
    n = len(holes)
    wormholes = set()
    for _ in range(n - 1):
        x1, y1, x2, y2 = map(int, input().split())
        wormholes.add((x1, y1))
        wormholes.add((x2, y2))

    grid = [[0] * n for _ in range(n)]
    for x, y in wormholes:
        grid[x][y] = 1

    max_holes = 0
    for i, (x, y) in enumerate(holes):
        if grid[x][y]:
            continue
        visited = set()
        dx, dy = 1, 0
        for _ in range(n + 3):
            nx, ny = x + dx * i, y + dy * i
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
            if grid[nx][ny]:
                visited.add((nx, ny))
            elif (nx, ny) == (x, y):
                max_holes = max(max_holes, len(visited))
                break
            dx, dy = -dy, dx
    return max_holes

T = int(input())
for _ in range(1, T + 1):
    n = int(input())
    holes = [list(map(int, input().split())) for _ in range(n)]
    print("Case #{}: {}".format(_, solve(holes)))


This code takes the number of test cases T as input, followed by the coordinates of each hole. For each test case, it reads the number of holes N and the coordinates of the holes, then calculates the maximum number of distinct holes that can be touched with a single hit by considering wormholes and recursively moving in all possible directions from each hole until reaching another hole or going out of bounds. The output is formatted as specified in the description.