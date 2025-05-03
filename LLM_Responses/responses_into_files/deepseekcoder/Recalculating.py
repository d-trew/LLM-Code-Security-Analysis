import sys
from collections import defaultdict
from heapq import heappop, heappush

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solve():
    T = int(input().strip())
    for t in range(T):
        n, d = map(int, input().split())
        centers = [tuple(map(int, input().split())) for _ in range(n)]
        
        # Create a priority queue to store the repair center locations relative to Principia's current location.
        pq = [(0, 0, 0)]
        visited = defaultdict(lambda: float('inf'))
        while pq:
            dist, x, y = heappop(pq)
            
            if dist > visited[(x, y)]: continue
            
            for nx, ny in centers:
                ndist = manhattan_distance(nx, ny, x, y)
                
                if ndist <= d and (ndist < visited[(nx - x, ny - y)] or ((ndist == visited[(nx - x, ny - y)]) and (nx < x))):
                    visited[(nx - x, ny - y)] = ndist
                    heappush(pq, (ndist, nx, ny))
        
        # Count the number of distinguishable locations.
        count = 0
        for dist in visited.values():
            if dist <= d: count += 1
                
        print("Case #{}: {}".format(t + 1, count))

if __name__ == "__main__":
    solve()