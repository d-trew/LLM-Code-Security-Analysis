Here is the Python code based on your description:


import sys
from heapq import *

def solve():
    input = sys.stdin.readline
    output = sys.stdout.write
    
    t = int(input())
    for case in range(1, t + 1):
        n, d = map(int, input().split())
        angles = list(map(int, input().split()))
        
        total_cuts = 0
        max_heap = [-angle for angle in angles]
        heapify(max_heap)  # convert the list into a heap
        
        while len(max_heap) >= d:
            largest_cut = -1 * heappop(max_heap)
            second_largest_cut = -1 * heappop(max_heap)
            
            total_cuts += 1
            if largest_cut - second_largest_cut > 0:
                heappush(max_heap, -second_largest_cut)  # push the remaining piece back to heap
                heappush(max_heap, -((largest_cut - second_largest_cut) / 2))
        
        output("Case #{}: {}\n".format(case, total_cuts if len(max_heap) == 0 else "impossible"))
    
if __name__ == '__main__':
    solve()

This program uses a priority queue (or max heap in this case) to keep track of the largest angles. It pops out two largest elements from the heap, increments total cuts by 1 and pushes back the remaining piece into the heap if it's larger than zero. This process continues until there are not enough pieces left for each diner or until all diners have been served. If at any point the largest angle is less than the second largest (which would mean we can't satisfy a diner with two slices), the program outputs "impossible".