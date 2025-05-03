import sys
from collections import defaultdict

def get_line_of_sight(x, y):
    return [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if 0 <= x + dx < R and 0 <= y + dy < C]

def get_soldier_moves(grid):
    soldier_moves = defaultdict(list)
    soldiers_positions = [(x, y) for y in range(R) for x in range(C) if grid[y][x] == 'S']
    for sx, sy in soldiers_positions:
        for tx, ty in [t for t in turret_positions if t not in soldier_moves[(sx, sy)]]:
            if (tx - sx) * (tx - sx) + (ty - sy) * (ty - sy) <= M * M:
                line_of_sight = get_line_of_sight(sx, sy)
                if tx in [t[0] for t in line_of_sight]:
                    soldier_moves[(sx, sy)].append((tx, ty))
    return soldier_moves

def count_destroyed_turrets(grid):
    destroyed = 0
    for x in range(R):
        for y in range(C):
            if grid[x][y] == 'T':
                destroyed += 1
    return destroyed

def main():
    T = int(input())
    for i in range(1, T + 1):
        C, R, M = map(int, input().split())
        grid = [list(input()) for _ in range(R)]
        turret_positions = [(x, y) for y in range(R) for x in range(C) if grid[y][x] == 'T']
        soldier_moves = get_soldier_moves(grid)
        max_destroyed_turrets = 0
        for sx, sy in sorted([pos for pos, moves in soldier_moves.items() if len(moves) > 0], key=lambda x: -len(soldier_moves[x])):
            destroyed_turrets = count_destroyed_turrets(grid)
            for tx, ty in sorted(soldier_moves[(sx, sy)]):
                grid[ty][tx] = '.'
                if len(get_line_of_sight(sx, sy)) > 0:
                    destroyed_turrets -= 1
            max_destroyed_turrets = max(max_destroyed_turrets, destroyed_turrets)
        print("Case #{}: {}".format(i), max_destroyed_turrets)

if __name__ == "__main__":
    main()