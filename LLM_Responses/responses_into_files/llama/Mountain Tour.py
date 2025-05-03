def solve(camps):
    dp = [[float('inf')] * camps for _ in range(23)]
    dp[0][0] = 0
    for i in range(1, 2*camps+1):
        start, end, duration = (i-1)//2, (i-1)//2 + ((i-1)%2)*2, (i-1) % 4 * 1000 + 1
        if dp[start][end-start] == float('inf'):
            continue
        for j in range(min(end, camps), end-duration):
            dp[j][j+duration] = min(dp[j][j+duration], dp[start][end-start] + duration)
    return min(dp[0])

for i in range(int(input())):
    camps = int(input())
    print(f"Case #{i+1}: {solve(camps)}")