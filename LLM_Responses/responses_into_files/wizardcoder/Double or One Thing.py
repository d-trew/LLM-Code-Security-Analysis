import sys
sys.setrecursionlimit(10**6)
T = int(input())
for i in range(1, T+1):
    S = input()
    result = ''
    for c in S:
        if c == 'H':
            result += 'HH'
        else:
            result += c*2
    print('Case #%d: %s' % (i, result)