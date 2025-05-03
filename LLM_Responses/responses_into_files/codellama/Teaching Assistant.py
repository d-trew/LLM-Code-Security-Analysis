import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    S = input()
    C = 0
    J = 0
    for i in range(len(S)):
        if S[i] == 'C':
            C += 1
        elif S[i] == 'J':
            J += 1
    max_points = max(C, J) * 5
    print("Case #" + str(t) + ": " + str(max_points))