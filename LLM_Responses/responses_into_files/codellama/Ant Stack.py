import sys

def solve(N, W):
    if N == 1:
        return 1
    else:
        max_stack = 0
        for i in range(1, N+1):
            if sum(W[0:i]) <= 6*W[i-1]:
                max_stack = max(max_stack, solve(N-i, W[i:]))
        return max_stack + 1

case = int(input())
for i in range(case):
    N = int(input())
    W = list(map(int, input().split()))
    print("Case #" + str(i+1) + ": " + str(solve(N, W)))