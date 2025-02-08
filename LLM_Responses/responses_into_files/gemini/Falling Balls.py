def solve():
    C = int(input())
    B = list(map(int, input().split()))

    if sum(B) != C:
        return "IMPOSSIBLE"

    grid = [['.' for _ in range(C)] for _ in range(C)]

    balls = [i for i in range(C)]
    
    for r in range(C):
        for c in range(C):
            if B[c] > 0:
                if balls[c] == c:
                    B[c] -=1
                else:
                    if balls[c] > c:
                        grid[r][c] = '\\'
                        balls[c] +=1

                    else:
                        grid[r][c] = '/'
                        balls[c] -= 1

    
    
    ans = []
    for row in grid:
        ans.append("".join(row))

    return C ,ans



T = int(input())
for i in range(1, T + 1):
    result = solve()
    if result == "IMPOSSIBLE":
        print(f"Case #{i}: IMPOSSIBLE")
    else:
        rows, grid = result
        print(f"Case #{i}: {rows}")
        for row in grid:
            print(row)