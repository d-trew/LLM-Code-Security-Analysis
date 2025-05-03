def hack_program(program):
    n = len(program)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n):
        if program[i-1] == 'S':
            dp[i] = min(dp[i], dp[i-1] + 1)
        elif program[i-1] == 'C' and i > 1:
            dp[i] = min(dp[i], dp[i-2] + 1)
    return 'IMPOSSIBLE' if dp[-1] == float('inf') else str(min(dp))

t = int(input())
for _ in range(t):
    d, program = input().split()
    d = int(d)
    print(f"Case #{_+1}: {hack_program(program)}")