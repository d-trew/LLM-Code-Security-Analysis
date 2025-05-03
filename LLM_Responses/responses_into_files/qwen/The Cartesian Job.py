import math
for _ in range(int(input())): 
    n = int(input())
    events = []
    for i in range(n):
        x0, y0, x1, y1 = map(int, input().split())
        r = (x1-x0)**2 + (y1-y0)**2
        events.append((r, 0 if y1 < 0 or y1 > 1000 else -1))
    events.sort()
    res = 1
    t = 0
    for event in events:
        r, flag = event
        t += math.sqrt(r)
        if flag == -1: 
            res *= (t % 2) / t
        t %= 1
    print(f"Case #{_+1}: {res:.6f}")