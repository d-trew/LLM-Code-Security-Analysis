Here's the Python code for this problem:


import sys
from heapq import heappop, heappush
def solve(n, m, s):
    events = [[] for _ in range(n+1)]
    duck_meetings = []
    for i in range(m):
        x, y, t = map(int, input().split())
        heappush(duck_meetings, (t, x, y))
    for _ in range(s):
        a, b, u, v, d = map(int, input().split())
        events[a].append((d, u, v))
        events[b].append((d, u, v))
    known_geese = [False]*(n+1)
    ans = 0
    while duck_meetings:
        _, x, y = heappop(duck_meetings)
        if not known_geese[x]:
            known_geese[x] = True
            ans += 1
        for e in events[x]:
            t, u, v = e
            if abs(u-x)**2 + abs(v-y)**2 > t**2: continue
            if not known_geese[u]:
                known_geese[u] = True
                ans += 1
    print("Case #{}: {}".format(_+1, ans))
T = int(input())
for _ in range(T):
    n, m, s = map(int, input().split())
    solve(n, m, s)