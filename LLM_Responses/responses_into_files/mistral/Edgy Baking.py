def cookie_cutter(N, P):
    cookies = []
    for _ in range(N):
        width, height = map(int, input().split())
        cookies.append((width, height))
    
    dp = [[0, [0, 0]]] * (P + 1)
    for w, h in cookies:
        for i in range(P, w * 2 + h * 2 - 2, -1):
            if i >= w * 2 + h * 2:
                dp[i][0] = max(dp[i][0], dp[i - w - h][0] + w + h)
            else:
                dp[i][0] = max(dp[i][0], min(dp[i - w][1][0] + w, dp[i - h][1][0] + h))
    
    return str(int(max(i[0] for i in dp[:P])))


T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    print(f"Case #{_+1}: {cookie_cutter(N, P)}")