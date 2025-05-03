def solve():
    T = int(input())
    for t in range(T):
        S = int(input())
        P = list(map(int, input().split()))
        
        MOD = 10**9 + 7
        ans = 0
        
        # Iterate over all possible values of L and R.
        for l in range(min(S-2, 500)):
            for r in range(l+1):
                # The remaining stacks are P[l], P[l+1], ..., P[S-r-1].
                stack = sorted(P[i] for i in range(l, S-r))
                
                # Calculate the pyramidification cost of the current sequence.
                cost = 0
                for i in range(len(stack)-1):
                    diff = stack[i] - stack[i+1] + 1
                    if diff > 0:
                        cost += diff
                
                ans += cost
        
        print("Case #{}: {}".format(t+1, ans % MOD))

solve()