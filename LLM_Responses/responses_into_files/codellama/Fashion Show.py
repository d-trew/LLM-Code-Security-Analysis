# Test cases
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    grid = [['.' for _ in range(N)] for _ in range(N)]
    pre_placed = []
    for i in range(M):
        type, row, col = input().split()
        if type == '+':
            grid[int(row) - 1][int(col) - 1] = '+'
        elif type == 'x':
            grid[int(row) - 1][int(col) - 1] = 'x'
        else:
            grid[int(row) - 1][int(col) - 1] = 'o'
        pre_placed.append((type, int(row), int(col)))
    # Find maximum number of style points
    max_points = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                continue
            point = 1
            if i > 0 and grid[i - 1][j] != '.':
                point += 2
            if j > 0 and grid[i][j - 1] != '.':
                point += 2
            if abs(i - j) > 0 and (grid[i - 1][j - 1] != '.' or grid[i + 1][j - 1] != '.' or grid[i - 1][j + 1] != '.' or grid[i + 1][j + 1] != '.'):
                point += 2
            max_points = max(max_points, point)
    # Find maximum number of models
    max_models = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                continue
            count = 1
            if i > 0 and grid[i - 1][j] != '.':
                count += 1
            if j > 0 and grid[i][j - 1] != '.':
                count += 1
            if abs(i - j) > 0 and (grid[i - 1][j - 1] != '.' or grid[i + 1][j - 1] != '.' or grid[i - 1][j + 1] != '.' or grid[i + 1][j + 1] != '.'):
                count += 1
            max_models = max(max_models, count)
    # Output
    print("Case #" + str(t + 1) + ": " + str(max_points) + " " + str(max_models))
    for type, row, col in pre_placed:
        if grid[row - 1][col - 1] == '.':
            continue
        print(type + " " + str(row) + " " + str(col))