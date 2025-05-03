def solve(S, D):
    MOD = 10**9+7
    n = len(S)
    
    dp = [0]*(n+2)
    dp[0] = 1
    prev_zero = [-1]*10
    curr_divisible = [False]*n
    
    for i in range(n):
        digit = int(S[i])
        for j in range(digit+1 if i > 0 else 1, 10):
            if prev_zero[j-1] != -1:
                dp[i+2] += dp[prev_zero[j-1]]
                dp[i+2] %= MOD
        for j in range(digit, 10):
            if not curr_divisible[i]:
                prev_zero[j] = i+1
    
    divisible = [False]*(n+1)
    stack = []
    for i in range(n-1,-1,-1):
        while stack and S[stack[-1]] < S[i]:
            stack.pop()
        if not stack:
            divisible[i] = True
        else:
            j = stack[-1]
            if (j-i+1)%D == 0 or ((S[i:j+1])%D == 0):
                divisible[i] = True
        stack.append(i)
    
    for i in range(n+1):
        if not divisible[i]: continue
        for j in range(i+2, n+2):
            dp[j] += dp[i]
            dp[j] %= MOD
            
    return dp[-1]

T = int(input())
for tc in range(1, T+1):
    S, D = input().split()
    print("Case #{}: {}".format(tc, solve(S, int(D))))