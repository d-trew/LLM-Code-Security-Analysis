import sys
from collections import defaultdict

def get_style(grid):
    style = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '+':
                style += 1
            elif grid[i][j] == 'x':
                style += 2
    return style

def get_neighbors(i, j):
    neighbors = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if abs(di) + abs(dj) == 1:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    neighbors.append((ni, nj))
    return neighbors

def is_valid(grid, i, j, model):
    for neighbor in get_neighbors(i, j):
        if grid[neighbor[0]][neighbor[1]] == '+':
            return True
    return False

def place_models(grid, models):
    for i, j, model in models:
        if is_valid(grid, i, j, model) and grid[i][j] != '.':
            grid[i][j] = model

def solve(N, M, pre_placed):
    grid = [['.' for _ in range(N)] for _ in range(N)]
    models = []
    for m in range(M):
        i, j, model = map(int, input().split())
        if i == 1:
            models.append((i-1, j-1, chr(model)))
        else:
            grid[i-1][j-1] = chr(model)
    place_models(grid, pre_placed + models)
    return get_style(grid), len(pre_placed) + len(models)

T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    pre_placed = []
    for _ in range(M-1):
        pre_placed.append(tuple(map(int, input().split())) + (ord(input()),))
    style, added = solve(N, M, pre_placed)
    print("Case #{}: {} {}".format(i, style))
    for model in sorted([chr(m[2]) + ' ' + str(m[0]+1) + ' ' + str(m[1]+1) for m in pre_placed + models]):
        print(model)