Here's a Python program based on your description. This code assumes you have all inputs available as separate variables named `T`, `N`, `C`, `A`, `B` and `P`. The code uses dynamic programming to solve the problem:


def count_choices(T, N, C, A, B, P):
    dp = [[0 for _ in range(N+1)] for _ in range(C+1)]
    
    # Initialize base case
    dp[0][0] = 1
    
    # Calculate DP table
    for i in range(1, C+1):
        for j in range(N+1):
            dp[i][j] = dp[i-1][j]
            if j >= A[i-1]:
                dp[i][j] += dp[i][j-A[i-1]]
            if j > B[i-1]:
                dp[i][j] -= dp[i-1][j-B[i-1]-1]
    
    # Calculate total choices for each test case
    choices = []
    for i in range(T):
        count = 0
        for j in range(2, N+1):
            if P[i] == 1:
                count += dp[C][j-1] - dp[P.count(1)-1][j-1]
            else:
                count += dp[C][j-1]
        choices.append(count)
    
    return choices


This code first calculates a dynamic programming (DP) table where `dp[i][j]` is the number of ways to select j geese out of i colors, and then uses this DP table to calculate the total number of valid selections for each test case. Note that we subtract dp[i-1][j-B[i]-1] because these are cases where the last selection was more than B_i, which is not allowed by the problem statement.