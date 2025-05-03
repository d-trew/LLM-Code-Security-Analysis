import sys
from math import pi
from heapq import nlargest

def solve(n, k):
    # Read input
    r = []
    h = []
    for _ in range(n):
        ri, hi = map(int, sys.stdin.readline().split())
        r.append(ri)
        h.append(hi)
    
    # Calculate surface area for each pancake and sort them in descending order
    areas = sorted([pi * (r[i]**2 + r[i] * h[i]) for i in range(n)], reverse=True)
    
    # Select the top k largest surfaces
    selected_areas = nlargest(k, areas)
    
    return sum(selected_areas)

# Read number of test cases
t = int(sys.stdin.readline())
for i in range(1, t + 1):
    n, k = map(int, sys.stdin.readline().split())
    result = solve(n, k)
    
    # Print the result
    print('Case #{}: {}'.format(i, result))