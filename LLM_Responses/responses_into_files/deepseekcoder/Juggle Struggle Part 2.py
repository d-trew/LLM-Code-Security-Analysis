import sys
from collections import namedtuple

Point = namedtuple('Point', 'x y')
Line = namedtuple('Line', 'p1 p2')

def direction(p, q, r):
    return (q.x - p.x)*(r.y - q.y) - (q.y - p.y)*(r.x - q.x)

def on_segment(p, q, r):
    return min(p.x, r.x) <= q.x <= max(p.x, r.x) and min(p.y, r.y) <= q.y <= max(p.y, r.y)

def do_intersect(line1, line2):
    p1, q1 = line1
    p2, q2 = line2
    
    d1 = direction(p1, q1, p2)
    d2 = direction(p1, q1, q2)
    d3 = direction(p2, q2, p1)
    d4 = direction(p2, q2, q1)
    
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    elif d1 == 0 and on_segment(p1, p2, q1):
        return True
    elif d2 == 0 and on_segment(p1, q2, q1):
        return True
    elif d3 == 0 and on_segment(p2, p1, q2):
        return True
    elif d4 == 0 and on_segment(p2, q1, q2):
        return True
    
    return False

def check_arrangement():
    n = int(sys.stdin.readline().strip())
    jugglers = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
        p1, p2 = Point(x1, y1), Point(x2, y2)
        jugglers.append((p1, p2))
    
    for i in range(n):
        for j in range(i+1, n):
            line_ij = Line(*jugglers[i])
            line_jk = Line(*jugglers[j])
            
            if do_intersect(line_ij, line_jk):
                return i, j
    
    return -1, -1

t = int(sys.stdin.readline().strip())
for case in range(1, t+1):
    pair = check_arrangement()
    if pair == (-1, -1):
        print("Case #{}: MAGNIFICENT".format(case))
    else:
        print("Case #{}: {}".format(case, " ".join(map(str, pair))))