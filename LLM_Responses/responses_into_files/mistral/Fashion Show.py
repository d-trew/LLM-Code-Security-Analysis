import sys
input = sys.stdin.readlines

def solve(n, m, grid):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    models = set()
    for i, row in enumerate(grid):
        if row == '.':
            continue
        models.add(row[0])
        dp[i + 1][int(row[2:])] += 1

    for i in range(n - 1, -1, -1):
        for j in range(1, n + 1):
            if (dp[i+1][j] == 0 and dp[i+1][j-1] > 0) or \
               (dp[i+1][j] == 1 and dp[i+1][j-1] > 1) or \
               (dp[i+1][j] == 2 and dp[i+1][j-1] >= 2):
                dp[i][j] = max(dp[i][j], dp[i+1][j-1] + dp[i][j-1])
            elif (dp[i+1][j] == 0 and dp[i+1][j+1] > 0) or \
                 (dp[i+1][j] == 1 and dp[i+1][j+1] > 1) or \
                 (dp[i+1][j] == 2 and dp[i+1][j+1] >= 2):
                dp[i][j] = max(dp[i][j], dp[i+1][j+1] + dp[i][j+1])
            if (i < n - 1) and (dp[i+2][j] > 0 or dp[i+2][j-1] > 0 or dp[i+2][j+1] > 0):
                diag_sum = dp[i+2][j] + dp[i+2][j-1] + dp[i+2][j+1]
                if (dp[i+1][j] == 0 and diag_sum > 0) or \
                   (dp[i+1][j] == 1 and 1 <= diag_sum <= 2) or \
                   (dp[i+1][j] == 2 and diag_sum >= 3):
                    dp[i][j] = max(dp[i][j], diag_sum + dp[i][j-1])

    max_points, max_models = max((val, len(set(val))) for val in zip(*dp[-1]))
    if max_points == 0:
        return []
    models_to_add = set()
    for i in range(1, n+1):
        if dp[n][i] == max_points and (i not in models or dp[1][i] < max_points):
            models_to_add.add('o')
    return ['Case #{}: {} {}'.format(tc+1, max_points, len(models_to_add)), *['{} {} 1'.format(t, i) for t, i in sorted(list(models_to_add))]]

T = int(input()[0].strip())
for _ in range(T):
    n, m = map(int, input()[0].split())
    grid = [input().strip() for _ in range(m)]
    print('\n'.join(solve(n, m, grid)))


This Python code reads the test cases from standard input and outputs the solution for each case. The solution consists of a list of strings representing the final grid, including the number of style points earned and the total number of models added or upgraded. The code uses dynamic programming to find the maximum possible number of style points and the optimal placement of additional models. The grid is represented as a 2D list where each cell can contain a character representing the type of model (if any) in that cell, or '.' if the cell is empty. The function `solve(n, m, grid)` takes the dimensions of the grid and its initial state as arguments and returns the solution as a list of strings.