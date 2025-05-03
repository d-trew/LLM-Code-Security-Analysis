import sys
input = sys.stdin.readline
B, S, N = map(int, input().split())
slides = {}
for i in range(N):
    x, y = map(int, input().split())
    if (x, y) not in slides:
        slides[(x, y)] = []
    slides[(x, y)].append(i)
states = [[] for _ in range(S+1)]
for i in range(N):
    states[i%(S+1)].append(slides[(i%B+1, (i+1)%B+1)])
fun = True
for i in range(N):
    if not fun:
        break
    op = input().split()
    L, R, M = map(int, op[2:5])
    if op[0] == 'E':
        for j in range(L, R+1, M):
            if states[j][-1]:
                fun = False
                break
    elif op[0] == 'D':
        for j in range(L, R+1, M):
            if not states[j][-1]:
                fun = False
                break
if fun:
    print('Case #{}:\n'.format(i+1), end='')
else:
    print('Case #{}:\n'.format(i+1), end='')
for i in range(N):
    if states[i%(S+1)][-1]:
        print(i+1, end=' ')