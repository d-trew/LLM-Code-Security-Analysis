import sys
input = sys.stdin.readlines

def destroy_turrets():
    t, cases = int(input()), []
    for _ in range(t):
        r, c, m = map(int, input().split())
        grid = [list(map(str, input())) for _ in range(r)]
        soldiers, turrets = set(), set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 'S':
                    soldiers.add((i, j))
                elif cell == 'T':
                    turrets.add((i, j))
        moves = [[(-1, 0), (1, 0), (0, -1), (0, 1)] for _ in range(len(soldiers))]
        for soldier in soldiers:
            turret_to_destroy = None
            bullets = m
            for move in moves[soldier]:
                next_pos = (soldier[0] + move[0], soldier[1] + move[1])
                if next_pos[0] < 0 or next_pos[0] >= r or \
                   next_pos[1] < 0 or next_pos[1] >= c or grid[next_pos[0]][next_pos[1]] != '.':
                    continue
                if grid[next_pos[0]][next_pos[1]] == 'T':
                    turret_to_destroy = (next_pos[0], next_pos[1])
                    break
            if not turret_to_destroy:
                continue
            bullets -= 1
            if bullets < 0:
                break
            grid[soldier[0]][soldier[1]] = '.'
            soldier = next_pos
            moves[soldier].remove((move[0], move[1]))
            if grid[turret_to_destroy[0]][turret_to_destroy[1]] in soldiers:
                turrets.remove(turret_to_destroy)
        cases.append(f"Case #{cases.index(case)+1}: {len(turrets)}")
    for case, turrets_left in enumerate(turrets):
        soldiers_moves = [[] for _ in range(len(soldiers))]
        for i, soldier in enumerate(soldiers):
            moves = [[(-1, 0), (1, 0), (0, -1), (0, 1)] for _ in range(m)]
            for move in moves[i]:
                next_pos = (soldier[0] + move[0], soldier[1] + move[1])
                if next_pos[0] < 0 or next_pos[0] >= r or \
                   next_pos[1] < 0 or next_pos[1] >= c or grid[next_pos[0]][next_pos[1]] != '.':
                    continue
                if grid[next_pos[0]][next_pos[1]] == 'T':
                    soldiers_moves[i].append((next_pos[0], next_pos[1]))
        for i, soldier in enumerate(soldiers):
            moves = soldiers_moves[i]
            if not moves:
                continue
            move = min(moves, key=lambda x: abs(x[0] - turrets_left[0]) + abs(x[1] - turrets_left[1]))
            soldiers_moves[i].remove(move)
            soldier = move
            m -= 1
            moves = [[(-1, 0), (1, 0), (0, -1), (0, 1)] for _ in range(len(soldiers))]
            grid[soldier[0]][soldier[1]] = '.'
            soldier = next_pos
            moves[soldier].remove((move[0], move[1]))
            if grid[turrets_left[0]][turrets_left[1]] in soldiers:
                turrets.remove(turrets_left)
        cases.append(f"Case #{case+1}: {len(turrets)}")
    for case in cases:
        print(case)

destroy_turrets()


This code reads the input from standard input and outputs the result for each test case as described. The soldiers are represented as a set, and their moves are stored in a list of lists. For each soldier, it checks all possible moves and finds the one that leads to a turret. If no such move is found, it continues to the next soldier. If a valid move is found, it removes that move from the list of moves for that soldier and sets the new position of the soldier. Then it checks if the newly reached cell contains a turret and if so, removes that turret from the set of remaining turrets.
After all soldiers have been processed, if any turrets remain, the code repeats the process for each remaining turret until no more turrets can be destroyed. The final output is printed to standard output.