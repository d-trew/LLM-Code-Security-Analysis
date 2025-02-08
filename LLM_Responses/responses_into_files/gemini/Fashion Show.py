def solve():
    N, M = map(int, input().split())
    models = []
    for _ in range(M):
        models.append(input().split())

    grid = [['.' for _ in range(N)] for _ in range(N)]
    for model in models:
        grid[int(model[1]) - 1][int(model[2]) - 1] = model[0]

    added_models = []
    style_points = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == '.':
                valid = True
                for mr in range(N):
                    for mc in range(N):
                        if grid[mr][mc] != '.':
                            if r == mr or c == mc or r + c == mr + mc or r - c == mr - mc:
                                valid = False
                                break
                    if not valid:
                        break
                if valid:
                    grid[r][c] = 'o'
                    added_models.append(['o', r + 1, c + 1])
                    style_points += 2

    for model in models:
        if model[0] in ['+', 'x']:
            style_points +=1

    for r in range(N):
        for c in range(N):
            if grid[r][c] == '+':
                style_points += 1
            elif grid[r][c] == 'x':
                style_points += 1
            elif grid[r][c] == 'o':
                style_points += 2

    return style_points, added_models


T = int(input())
for i in range(1, T + 1):
    style_points, added_models = solve()
    print(f"Case #{i}: {style_points} {len(added_models)}")
    for model in added_models:
        print(*model)