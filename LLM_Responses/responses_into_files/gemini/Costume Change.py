def solve():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    changes = 0
    rows = [{} for _ in range(N)]
    cols = [{} for _ in range(N)]

    for r in range(N):
        for c in range(N):
            val = grid[r][c]
            if val in rows[r]:
                rows[r][val] +=1
            else:
                rows[r][val] = 1
            if val in cols[c]:
                cols[c][val] +=1
            else:
                cols[c][val] = 1

    for r in range(N):
        for c in range(N):
            val = grid[r][c]
            if rows[r][val] > 1 or cols[c][val] > 1:
                changes += 1

    return changes


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")