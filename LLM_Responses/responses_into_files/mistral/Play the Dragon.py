import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        hd, ad, hk, ak, b, d = map(int, input().split())
        dp = [float('inf') * (ak + 1) for _ in range(hd + 1)]
        dp[0] = 0

        for i in range(1, hd + 1):
            for j in range(min(ak + 1, i), -1, -1):
                dp[i] = min(dp[i], dp[i - j] + 1)
                if j < ak:
                    dp[i] = min(dp[i], dp[i - (j + ak)] + ad)

        print('Case #{}: {}'.format(_ + 1, min(dp[-1], hk)))

solve()