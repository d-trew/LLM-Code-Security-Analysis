def solve():
    R, C = map(int, input().split())
    grid = []
    for _ in range(R):
        grid.append(list(map(int, input().split())))

    total_interest = 0
    
    while True:
        round_interest = 0
        eliminated = False
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] != -1:
                    round_interest += grid[r][c]

        total_interest += round_interest
        
        to_eliminate = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == -1:
                    continue

                neighbors = []
                # Check up
                for i in range(r - 1, -1, -1):
                    if grid[i][c] != -1:
                        neighbors.append(grid[i][c])
                        break
                    elif grid[i][c] == -1:
                        break

                # Check down
                for i in range(r + 1, R):
                    if grid[i][c] != -1:
                        neighbors.append(grid[i][c])
                        break
                    elif grid[i][c] == -1:
                        break

                # Check left
                for j in range(c - 1, -1, -1):
                    if grid[r][j] != -1:
                        neighbors.append(grid[r][j])
                        break
                    elif grid[r][j] == -1:
                        break

                # Check right
                for j in range(c + 1, C):
                    if grid[r][j] != -1:
                        neighbors.append(grid[r][j])
                        break
                    elif grid[r][j] == -1:
                        break

                if neighbors:
                    avg_neighbor = sum(neighbors) / len(neighbors)
                    if grid[r][c] < avg_neighbor:
                        to_eliminate.append((r, c))
                        eliminated = True

        for r, c in to_eliminate:
            grid[r][c] = -1

        if not eliminated:
            break

    return total_interest


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")