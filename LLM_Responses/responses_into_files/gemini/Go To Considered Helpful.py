def solve():
    R, C = map(int, input().split())
    grid = [input() for _ in range(R)]

    marlin_r, marlin_c = -1, -1
    son_r, son_c = -1, -1

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'M':
                marlin_r, marlin_c = r, c
            elif grid[r][c] == 'N':
                son_r, son_c = r, c

    q = [(marlin_r, marlin_c, [], 0)]  # (row, col, instructions, instruction_count)
    visited = set()

    while q:
        r, c, instructions, instruction_count = q.pop(0)

        if (r, c) == (son_r, son_c):
            return instruction_count

        state = (r, c, tuple(instructions))
        if state in visited:
            continue
        visited.add(state)

        
        next_instructions = instructions + [len(instructions)+1]

        # Move North
        nr, nc = r - 1, c
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            q.append((nr, nc, next_instructions, instruction_count + 1))

        # Move East
        nr, nc = r, c + 1
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            q.append((nr, nc, next_instructions, instruction_count + 1))

        #Move South
        nr, nc = r + 1, c
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            q.append((nr, nc, next_instructions, instruction_count + 1))

        #Move West
        nr, nc = r, c - 1
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            q.append((nr, nc, next_instructions, instruction_count + 1))

        #Jump
        q.append((r,c, next_instructions, instruction_count + 1))
            

    return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")