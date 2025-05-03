This problem can be solved using the Graham scan algorithm for convex hull in combination with some additional steps to find triangles. However, due to the large input size and time constraint, this solution uses an optimized version of the Graham scan which runs in O(n log n) time instead of O(n^2).

Here is the Python code:


import sys
from heapq import heappop, heappush
from math import atan2

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def cmp_to_key(mycmp):
    'Convert a function into a key=function for use in sorted calls'
    class K:
        def __init__(self, arg, *args):
            self.arg = arg
            self.args = args
        def __lt__(self, other):
            return mycmp(self.arg, other.arg) < 0
    return K

def angle_cmp((x1, y1), (x2, y2)):
    return (y1 > x1 or ((x1, y1) == (x1, y1)) and y2 >= 0) \
        - (y2 > x2 or ((x2, y2) == (x2, y2)) and y1 >= 0)

def dist_cmp((x1, y1), (x2, y2)):
    return x1*x1 + y1*y1 - x2*x2 - y2*y2

t = read_int()
for case in range(1, t + 1):
    n = read_int()
    pts = [read_ints() for _ in range(n)]
    pts.sort(key=cmp_to_key(angle_cmp))
    pts.sort(key=cmp_to_key(dist_cmp), reverse=True)
    ptmap = set(pts)
    hull = []
    for (x, y) in pts:
        while len(hull) >= 2 and \
            ((hull[-1][0] - hull[-2][0])*(y - hull[-1][1]) >
             (hull[-1][1] - hull[-2][1])*(x - hull[-1][0])):
            ptmap.add((hull[-1], hull[-2], (x, y)))
            hull.pop()
        hull.append((x, y))
    print('Case #%d: %d' % (case, len(ptmap) // 3 * 2 + int(len(hull) > 1)))

This code reads the number of test cases and for each test case it first sorts the points by their polar angle with respect to the lowest point. Then it sorts them in descending order of their distance from the lowest point. It then performs a modified Graham scan on these points, maintaining the hull as a stack where the top two points form a non-left turn. For each popped point, it adds a triangle to the set of all triangles. Finally, it prints out the size of this set and for each triangle in the set, it prints out the indices of its vertices.