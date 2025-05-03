import sys
from collections import defaultdict
input = sys.stdin.readlines

def solve():
    n, k = map(int, input().split())
    x, t = zip(*(map(list, (input(), input().split()))))
    x.append(k)
    x.sort()

    thermometers = defaultdict(int)
    temp_min = 184
    num_thermometers = 0

    for i in range(len(x)-1):
        if t[i] != t[i+1]:
            thermometers[x[i]] += 1
            if thermometers[x[i]] > 1:
                num_thermometers -= (thermometers[x[i]] - 1)
            temp_min = min(temp_min, t[i])

    for i in range(len(x)-1):
        if t[i] == t[i+1]:
            thermometers[x[i]] += 1
            if thermometers[x[i]] > 1:
                num_thermometers -= (thermometers[x[i]] - 1)
            temp_min = min(temp_min, t[i])

    for i in range(len(x)-1):
        if x[i+1] - x[i] > 1:
            diff = (x[i+1] - x[i]) // 2
            thermometers[(x[i] + diff)] += 1
            num_thermometers += 1
            temp_min = min(temp_min, t[int((i+1)/2)])

    for i in range(len(x)-1):
        if x[i+1] - x[i] == 1:
            thermometers[x[i]] += 1
            num_thermometers += 1
            temp_min = min(temp_min, max(t[int(i/2)], t[int((i+1)/2)]))

    if temp_min + 1 > 330:
        print("Case #x: Impossible")
    else:
        print("Case #x: {}".format(num_thermometers))

for _ in range(int(input())):
    solve()