import sys

sys.setrecursionlimit(10**6)

def min_operations(lst):
    n = len(lst)
    if n == 1:
        return lst[0]
    elif n == 2:
        if lst[0] < lst[1]:
            return lst[1] - lst[0]
        else:
            return 0
    else:
        dp = [0]*n
        for i in range(n):
            dp[i] = float('inf')
        dp[0] = 0
        dp[1] = lst[1] - lst[0] if lst[1] > lst[0] else 0
        for i in range(2, n):
            for j in range(i-1, -1, -1):
                if lst[j] < lst[i]:
                    dp[i] = min(dp[i], dp[j]+(lst[i]-lst[j])+1)
        return dp[-1]

T = int(input())
for i in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    print("Case #%d: %d" % (i, min_operations(lst))

# Time Complexity : O(N^2)