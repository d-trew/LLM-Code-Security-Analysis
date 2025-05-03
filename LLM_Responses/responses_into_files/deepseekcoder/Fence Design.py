import sys

def solve(n, poles, fences):
    dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in range(2, n + 1):
        for j in range(i - 1, -1, -1):
            if not dp[i][j]:
                for k in range(j + 1, i):
                    if set(poles[k]) & set(range(j, i)):
                        dp[i][j] = [(i, k)]
                        break
                if not dp[i][j]:
                    for k in range(j + 1, i):
                        if (poles[j][0] - poles[i][0]) * (poles[k][1] - poles[j][1]) == (poles[j][1] - poles[i][1]) * (poles[k][0] - poles[j][0]):
                            dp[i][j] = [(i, k)]
                            break

    return len(dp[-1][fences[1]]) + 2

T = int(input())
for case in range(1, T + 1):
    n = int(input())
    poles = [list(map(int, input().split())) for _ in range(n)]
    fences = [int(x) - 1 for x in map(int, input().split())]
    result = solve(n, poles, fences)
    print('Case #{}: {}'.format(case, result))
    if case == T:
        continue
    for i, j in enumerate(dp[-1][fences[1]], start=1):
        print(' '.join(map(str, [i + 1, j + 1])))