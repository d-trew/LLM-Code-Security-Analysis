import sys
input = sys.stdin.readline

def min_button_presses(N, Ps):
    dp = [[0] * (max(Ps) + 1) for _ in range(N)]
    for i, p in enumerate(Ps):
        for j in range(min(p), max(p) + 1):
            if not i or dp[i-1][j] < dp[i][j]:
                dp[i][j] = dp[i-1][j] + 2 * (j - dp[i-1][j]) if j > dp[i-1][j] else dp[i-1][j] + 1
            elif j - dp[i-1][j] < dp[i][j] - dp[i-1][j]:
                dp[i][j] = dp[i-1][dp[i-1][j]] + dp[i][j] - dp[i-1][j]
    return sum(dp[-1])

T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    Ps = [list(map(int, input().split())) for _ in range(N)]
    print("Case #{}: {}".format(_ + 1, min_button_presses(N, Ps)))