#!/bin/python3
import sys
input = sys.stdin.readline
T = int(input())
for t in range(1, T+1):
    X, Y, S = input().split()
    count_CJ = 0
    count_JC = 0
    for i in range(len(S)):
        if S[i] == 'C':
            if S[i+1] == 'J':
                count_CJ += 1
        elif S[i] == 'J' and S[i+1] == 'C':
            count_JC += 1
    print("Case #" + str(t) + ": " + str(count_CJ * X + count_JC * Y))