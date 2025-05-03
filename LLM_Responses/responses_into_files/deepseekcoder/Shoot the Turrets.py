def solve(C, R, M, grid):
    soldiers = [(i, j) for i in range(R) for j in range(C) if grid[i][j] == 'S']
    turrets = [(i, j) for i in range(R) for j in range(C) if grid[i][j] == 'T']

    def dfs(i, j, soldiers_left, turrets_left):
        if (i, j) in soldiers_left:
            soldiers_left.remove((i, j))
        if (i, j) in turrets_left:
            turrets_left.remove((i, j))

        max_turrets_destroyed = 0
        for si, sj in soldiers_left:
            for ti, tj in turrets_left:
                if abs(si - i) + abs(sj - j) <= M and all(abs(si - ki) + abs(sj - kj) > M or (ki, kj) not in turrets_left for ki, kj in turrets_left):
                    destroyed = 1
                    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        ni, nj = i + di, j + dj
                        while 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != '#':
                            if grid[ni][nj] == 'T' and all(abs(si - ki) + abs(sj - kj) > M or (ki, kj) not in turrets_left for ki, kj in turrets_left):
                                destroyed += 1
                                break
                            ni, nj = ni + di, nj + dj
                    if destroyed:
                        max_turrets_destroyed = max(max_turrets_destroyed, 1 + dfs(i, j, soldiers_left[:], turrets_left[destroyed:]))

        return max_turrets_destroyed

    for i in range(len(soldiers)):
        for j in range(C):
            if grid[i][j] == 'T':
                grid[i][j] = '#'
    return str(max([dfs(i, 0, soldiers[:], turrets[:]) for i in range(R)]))