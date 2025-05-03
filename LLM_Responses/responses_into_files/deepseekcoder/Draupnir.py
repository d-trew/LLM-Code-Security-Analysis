from collections import deque
import sys
input = sys.stdin.readline

def count_rings():
    T, W = map(int, input().split())
    dp = [0] * (W+1)
    for _ in range(T):
        X, M = map(int, input().split())
        queue = deque([[X, 0]])
        while queue:
            x, w = queue.popleft()
            if dp[w] < x:
                dp[w] = x
            if w+1 <= W and (not queue or queue[-1][1] != w+1):
                queue.append([x, w+1])
        while M > 0:
            _, m_w = map(int, input().split())
            print(dp[m_w % (W+1)])
            M -= 1
    return dp