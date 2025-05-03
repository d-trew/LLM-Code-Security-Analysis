import sys
input = sys.stdin.readlines

def solve():
    T = int(next(input()))
    for _ in range(T):
        C = int(next(input()))
        tours = [list(map(int, next(input()).split())) for _ in range(2*C)]
        dp = [[float('inf')] * (24 + 1) for _ in range(C+1)]
        dp[0][0] = 0
        for i, [e, l, d] in enumerate(tours):
            for j in range(min(e, C)):
                dp[e][max(0, l - d + 1)] = min(dp[e][max(0, l - d + 1)], dp[j][l])
        ans = float('inf')
        for i in range(C):
            if dp[i][23] < float('inf'):
                ans = min(ans, dp[i][23])
        print("Case #{}: {}".format(_ + 1, ans))

solve()


This code reads the number of test cases and then iterates through each test case. For each test case, it initializes a 2D array dp to store the minimum time required to reach each camp at each hour. The base case is that it takes 0 hours to be at camp 0 at hour 0. Then, for each tour, it updates the dp array by considering all possible starting camps j and setting the minimum time to be the minimum of the current value (if any) and the time required to reach the starting camp plus the duration of the tour. Finally, it finds the minimum time among all the possible end camps that is not equal to infinity, which represents the optimal solution for the test case.