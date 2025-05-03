import sys
input = sys.stdin.readline

T = int(input())
for case in range(1, T+1):
    N = int(input())
    P = input().strip()
    E = []
    S = []
    for i in range(N-2):
        if P[i] == 'E':
            E.append(i)
        elif P[i] == 'S':
            S.append(i)
    result = ''
    for i in range(N-2):
        if i not in E and i not in S:
            result += 'E'
        else:
            result += 'S'
    print('Case #{}'.format(case), result)