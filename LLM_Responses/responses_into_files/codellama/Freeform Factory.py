#!/bin/python3
import sys
def solve(N, can_operate):
    # Write your code here.
    num_lessons = 0
    for i in range(N):
        for j in range(N):
            if can_operate[i][j] == '1':
                num_lessons += 1
    return num_lessons * 1
if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        N = int(input().strip())
        can_operate = []
        for i in range(N):
            can_operate.append(list(input().strip()))
        result = solve(N, can_operate)
        print("Case #" + str(a0+1) + ": " + str(result))