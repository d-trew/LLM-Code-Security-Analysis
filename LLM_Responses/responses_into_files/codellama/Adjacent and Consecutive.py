import sys
input = sys.stdin.readline
N = int(input())

for i in range(1, N+1):
    Mi, Ci = map(int, input().split())
    if (Mi == 3 and Ci == 2) or (Mi == 4 and Ci == 1):
        break
if i % 2:
    a_mistake = True
else:
    b_mistake = True
for j in range(i+1, N+1):
    Mi, Ci = map(int, input().split())
    if (Mi == 3 and Ci == 4) or (Mi == 2 and Ci == 3):
        a_mistake = False
        break
for k in range(j+1, N+1):
    Mi, Ci = map(int, input().split())
    if (Mi == 4 and Ci == 3) or (Mi == 1 and Ci == 2):
        b_mistake = False
        break
print("Case #x:", a_mistake + b_mistake)