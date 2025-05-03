MOD = 10**9 + 7

def can_fill(R, C, N, D, grid):
    for i in range(R):
        for j in range(C):
            if (i, j) not in grid:
                valid = True
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < R and 0 <= nj < C and (ni, nj) in grid:
                        if abs(grid[(i, j)] - grid[(ni, nj)]) > D:
                            valid = False
                            break
                if not valid:
                    return False
    return True

def max_sum(R, C, N, D, grid):
    for i in range(R):
        for j in range(C):
            if (i, j) not in grid:
                grid[(i, j)] = 0
    
    for _ in range(10):  # Try up to 10 times to improve the solution
        changed = False
        for i in range(R):
            for j in range(C):
                if (i, j) not in grid:
                    valid_values = [grid[(ni, nj)] for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if 0 <= ni < R and 0 <= nj < C and (ni, nj) in grid]
                    min_val = min(valid_values) - D
                    max_val = max(valid_values) + D
                    grid[(i, j)] = (min_val + max_val) // 2
                    changed = True
        if not changed:
            break
    
    return sum(grid.values()) % MOD

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        R = int(data[index])
        C = int(data[index + 1])
        N = int(data[index + 2])
        D = int(data[index + 3])
        grid = {}
        
        index += 4
        
        for _ in range(N):
            ri = int(data[index]) - 1
            ci = int(data[index + 1]) - 1
            bi = int(data[index + 2])
            grid[(ri, ci)] = bi
            index += 3
        
        if can_fill(R, C, N, D, grid):
            result = max_sum(R, C, N, D, grid)
        else:
            result = "IMPOSSIBLE"
        
        results.append(result)
    
    for i, res in enumerate(results, 1):
        print(f"Case #{i}: {res}")

solve()