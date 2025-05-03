import heapq
from math import sqrt

def euclidean_distance(point1, point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def solve():
    N = int(input())
    children = []
    sweets = [None] * (N+1)
    
    for _ in range(N):
        x, y = map(int, input().split())
        children.append((x,y))
        
    for i in range(1, N+1):
        x, y = map(int, input().split())
        sweets[i] = (x,y)
    
    # Sort the children by their initial position
    children.sort()
    
    # Create a priority queue to hold the distances and corresponding indices of the sweets
    pq = [(euclidean_distance(children[0], sweets[i]), i) for i in range(1, N+1)]
    heapq._heapify_max(pq)  # Priority queue with max-heap property
    
    result = []
    while pq:
        _, idx = heapq.heappop(pq)
        if not pq or pq[0][0] < euclidean_distance(children[len(result)+1], sweets[idx]):
            # The closest sweet to the next child is this one, so assign it
            result.append((len(result)+1, idx))
        else:
            # There exists a sweet that is closer to the next child than this one
            heapq.heappush(pq, (euclidean<｜begin▁of▁sentence｜>