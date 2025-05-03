def solve(R, C, F, S, grid_start, grid_end):
    def get_diff():
        diff = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if grid_start[i][j] != grid_end[i][j]:
                    diff[i][j] = 1
        return diff
    
    def get_min_cost():
        min_cost = sum([sum(row) for row in grid_start]) * F
        changes = get_diff()
        
        # Try to change all the tiles with one operation (flip or swap).
        if any(changes):
            flips = [[0]*C for _ in range(R)]
            swaps = 2*sum([row.count('MG') + row.count('GM') for row in changes])
            
            # Try to flip the tiles with one operation and see if it's better than current min_cost.
            for i in range(R):
                for j in range(C-1):
                    if changes[i][j] == changes[i][j+1] == 1:
                        flips[i][j], flips[i][j+1] = 1, 1
                        cost = sum([sum(row) for row in flips]) * F + swaps * S
                        if cost < min_cost:
                            min_cost = cost
                            
            # Try to swap the tiles with one operation and see if it's better than current min_cost.
            flips = [[0]*C for _ in range(R)]
            swaps = 2*(sum([row.count('MG') + row.count('GM') for row in changes]) - 1)
            for i in range(R-1):
                if changes[i][0] == changes[i+1][0] == 1:
                    flips[i][0], flips[i+1][0] = 1, 1
                    cost = sum([sum(row) for row in flips]) * F + swaps * S
                    if cost < min_cost:
                        min_cost = cost
                        
        return min_cost
    
    t = int(input())
    for case in range(1, t+1):
        R, C, F, S = map(int, input().split())
        grid_start = [list(input().strip()) for _ in range(R)]
        grid_end = [list(input().strip()) for _ in range(R)]
        print('Case #{}: {}'.format(case, get_min_cost()))
        
solve(*[int(x) for x in input().split()], [[char for char in input().strip()] for _ in range(R)], [[char for char in input().strip()] for _ in range(R)])