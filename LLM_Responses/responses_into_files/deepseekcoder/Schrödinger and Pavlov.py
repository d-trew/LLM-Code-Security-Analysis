from collections import defaultdict
MOD = 10**9+7
N = 5005
inv2 = pow(2, MOD-2, MOD)
dp = [[0]*3 for _ in range(N)]
cat = [False]*N
next_box = [-1]*N
tunnel = defaultdict(int)
test_cases = int(input())
for tc in range(1, test_cases+1):
    n = int(input())
    s = input()
    for i in range(n-1, -1, -1):
        if s[i] == 'C': cat[i] = True
        elif s[i] == '.': cat[i] = False
        else: next_box[i] = int(input())
    dp[0][0] = 2 if cat[0] else 1
    for i in range(1, n):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) * (not cat[i]) % MOD
        dp[i][1] = ((dp[i-1][2] if next_box[i-1] == -1 else dp[next_box[i-1]][0]) + dp[i-1][1]) * (not cat[i]) % MOD
        dp[i][2] = ((dp[i-1][2] if next_box[i-1] == -1 else dp[next_box[i-1]][0]) + dp[i-1][1]) * (cat[i]) % MOD
    print("Case #{}: {}".format(tc, (dp[-1][2]+dp[-1][1]-1*inv2)%MOD))