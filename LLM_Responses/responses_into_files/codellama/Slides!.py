import sys

def solve(B, M):
    if B == 1:
        return "POSSIBLE"
    elif B == 2 and M == 1:
        return "IMPOSSIBLE"
    else:
        return "POSSIBLE"

for case in range(1, int(input()) + 1):
    B, M = map(int, input().split())
    print("Case #{}".format(case))