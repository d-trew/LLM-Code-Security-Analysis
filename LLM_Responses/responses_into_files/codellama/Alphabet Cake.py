T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    grid = [input() for _ in range(R)]
    initial_to_child = {}
    child_to_initials = {}
    for i in range(R):
        for j in range(C):
            if grid[i][j] != '?':
                initial = grid[i][j]
                if initial not in initial_to_child:
                    initial_to_child[initial] = len(child_to_initials)
                    child_to_initials[len(child_to_initials)] = set()
                child_to_initials[initial_to_child[initial]].add((i, j))
    for i in range(len(child_to_initials)):
        for (r1, c1), (r2, c2) in itertools.combinations(list(child_to_initials[i]), 2):
            if r1 == r2 and abs(c1 - c2) > 0:
                row = [(c1, i)] * (c2 - c1 + 1)
                for r, (c, _) in enumerate(grid):
                    if r not in [r1, r2]:
                        grid[r] += 'a'
                    else:
                        for cc in range(c1, c2+1):
                            if r == r1 and c == c1:
                                grid[r] = list(grid[r])
                                grid[r][cc - c1] = initial_to_child[chr(ord('A') + i)]
                                grid[r] = ''.join(grid[r])
                            elif r == r2 and c == c2:
                                grid[r] = list(grid[r])
                                grid[r][cc - c1] = initial_to_child[chr(ord('A') + i)]
                                grid[r] = ''.join(grid[r])
                break
    print(f"Case #{'%d'%_}:")
    for row in grid:
        print(row)