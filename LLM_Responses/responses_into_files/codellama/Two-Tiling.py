import re

def solve_case(case):
    board = [list(line) for line in case[:3]]
    tile1 = [list(line) for line in case[3:6]]
    tile2 = [list(line) for line in case[6:]]

    def is_valid_red_pattern(pattern):
        return all(all(c == '@' or c == '.' and (c == '@' or c in pattern[0][1:]) for c in row) for row in pattern)

    valid_tiles = []
    for i in range(2**64):
        red_cells = [int(c) for line in [(j & 1 << k) for j, k in zip(*[[int(c) for c in line] for line in board])) for c in line if c == '@']
        pattern = [[0 if c == '.' else 1 for c in line] for line in board]
        is_solvable = True
        for tile in [tile1, tile2]:
            tile_pattern = [[(j & 1 << k) for j, k in zip(*[[int(c) for c in line] for line in tile])) for line in tile]
            if not all(all(pattern[i][j] == tile_pattern[i][j] and pattern[i][j] != 0 or c != '@' for i, j in zip(*[[i, j] for i, j in enumerate(line)])) for line in board):
                is_solvable = False
                break
        if is_solvable:
            valid_tiles.append(red_cells)

    return 'POSSIBLE' if any(valid_tiles) else 'IMPOSSIBLE'

T = int(input())
for t in range(1, T + 1):
    case = [list(line) for line in [input().strip() for _ in range(4)]]
    print(f"Case #{t}: {solve_case(case)}")
    if solve_case(case) == 'POSSIBLE':
        board = [['.' for _ in range(8)] for _ in range(8)]
        red_cells = valid_tiles[0]
        for i, j in zip(*[[i, j] for i, j in enumerate(board)]):
            if red_cells[i*8 + j]:
                board[i][j] = '@'
        for line in [str(''.join(['.' if c == '.' else '@' if i < 3 and j < 3 else ' ' for c in line])) for line in board]:
            print(line)