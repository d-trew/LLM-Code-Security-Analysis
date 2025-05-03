import sys
from collections import defaultdict
from heapq import heappop, heappush
from math import gcd

def read_ints():
    return map(int, sys.stdin.readline().split())

def solve():
    n = int(sys.stdin.readline())
    points = [tuple(read_ints()) for _ in range(n)]
    
    if n <= 1:
        print("Case #{}: {}".format(_+1, 1))
        return
        
    gcds = defaultdict(int)
    maxgcd = 0
    
    for i in range(n):
        xi, yi = points[i]
        for j in range(i + 1, n):
            xj, yj = points[j]
            
            dx, dy = xj - xi, yj - yi
            g = abs(gcd(dx, dy))
            
            if (dx // g, dy // g) in gcds:
                maxgcd = max(maxgcd, gcds[(dx // g, dy // g)] + 1)
                
            gcds[(dx // g, dy // g)] = max(gcds[(dx // g, dy // g)], 2 if (xi + yi) % 2 == 0 else 3)
            
    print("Case #{}: {}".format(_+1, n - maxgcd))

T = int(sys.stdin.readline())
for _ in range(T):
    solve()