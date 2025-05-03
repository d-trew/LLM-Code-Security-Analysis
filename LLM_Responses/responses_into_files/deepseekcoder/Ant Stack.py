def solve():
    T = int(input())
    for case in range(1, T + 1):
        N = int(input())
        weights = list(map(int, input().split()))
        dp = [0] * (N+2)
        ans = 0
        stack_size = 0
        
        for weight in reversed(weights):
            if stack_size == 0 or stack_size + 1 >= len(dp):
                dp[stack_size] = max(dp[stack_size], weight)
                ans = max(ans, stack_size+1)
            elif dp[stack_size+1] > weight:
                if dp[stack_size]:
                    dp[stack_size-1] = max(dp[stack_size-1], dp[stack_size])
                    ans = max(ans, stack_size)
            else:
                dp[stack_size+1] = weight
        print("Case #{}: {}".format(case, ans))
        
solve()