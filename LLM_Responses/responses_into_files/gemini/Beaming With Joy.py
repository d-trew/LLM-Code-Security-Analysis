def solve():
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]

    shooters = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '-' or grid[r][c] == '|':
                shooters.append((r, c))

    def simulate(orientation):
        covered = set()
        destroyed = set()

        for r, c in shooters:
            direction = orientation[shooters.index((r,c))]
            
            curr_r, curr_c = r, c
            if direction == 0: # -
                while 0 <= curr_c < C:
                    if (curr_r, curr_c) in destroyed:
                        break
                    if grid[curr_r][curr_c] == '#':
                        break
                    covered.add((curr_r, curr_c))
                    curr_c += 1
            else: # |
                while 0 <= curr_r < R:
                    if (curr_r, curr_c) in destroyed:
                        break
                    if grid[curr_r][curr_c] == '#':
                        break
                    covered.add((curr_r, curr_c))
                    curr_r += 1

        for r,c in shooters:
            if (r,c) in covered and (r,c) not in destroyed:
                destroyed.add((r,c))


        empty_cells = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.':
                    empty_cells += 1

        if len(covered) >= empty_cells and len(destroyed) == 0:
            return True, orientation
        else:
            return False, orientation
    
    for i in range(2**len(shooters)):
        binary = bin(i)[2:].zfill(len(shooters))
        orientation = [int(bit) for bit in binary]
        possible, final_orientation = simulate(orientation)
        if possible:
            
            for k in range(len(shooters)):
                r,c = shooters[k]
                if final_orientation[k] == 0:
                    grid[r][c] = '-'
                else:
                    grid[r][c] = '|'

            return "POSSIBLE\n" + "\n".join("".join(row) for row in grid)

    return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")