MOD = 1000000007

def solve():
    R, C, N, D = map(int, input().split())
    cells = []
    for _ in range(N):
        cells.append(list(map(int, input().split())))

    grid = {}
    for r, c, b in cells:
        grid[(r, c)] = b

    def is_valid(r, c):
        return 1 <= r <= R and 1 <= c <= C

    def check_constraints():
        for r, c in grid:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc):
                    if (nr, nc) in grid:
                        if abs(grid[(r, c)] - grid[(nr, nc)]) > D:
                            return False
        return True

    def calculate_sum():
        total_sum = 0
        for value in grid.values():
            total_sum = (total_sum + value) % MOD
        return total_sum

    
    def fill_grid(r,c):
        if r > R:
            if check_constraints():
                return calculate_sum()
            else:
                return -1

        nr, nc = r, c+1
        if nc > C:
            nr, nc = r+1, 1
        
        if (r,c) not in grid:
            max_sum = -1
            for b in range(1,2001):
                grid[(r,c)] = b
                res = fill_grid(nr,nc)
                if res != -1:
                    max_sum = max(max_sum,res)
                del grid[(r,c)]
            return max_sum
        else:
            return fill_grid(nr,nc)

    result = fill_grid(1,1)
    if result == -1:
        return "IMPOSSIBLE"
    else:
        return result

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")