import heapq
import math

def optimal_cut(N, P, cookies):
    # Calculate the perimeter of each cookie and its area
    perimeters = [2 * (wi + hi) for wi, hi in cookies]
    areas = [wi * hi for wi, hi in cookies]
    
    # Initialize a heap to store the differences between actual and desired perimeter sums
    diff_heap = []
    
    while True:
        # Calculate the current total area of all cookies
        total_area = sum(areas)
        
        # If the total area is greater than or equal to P, return the maximum possible perimeter sum
        if total_area >= P:
            max_perimeter = 2 * (P // N) + (total_area - P) / N
            while diff_heap and diff_heap[0][0] > max_perimeter:
                heapq.heappop(diff_heap)
            return 2 * max_perimeter if diff_heap else max_perimeter
        
        # If the total area is less than P, remove the cookie with the largest perimeter and add its difference to the heap
        max_idx = areas.index(max(areas))
        max_perimeter = perimeters[max_idx]
        heapq.heappush(diff_heap, (max_perimeter - 2 * math.sqrt(cookies[max_idx][0] * cookies[max_idx][1]), max_idx))
        
        # Update the perimeter and area of the removed cookie
        del perimeters[max_idx], areas[max_idx]
        
        if not diff_heap:
            return 2 * (P // N) + sum(perimeters) / N
        
        max_diff, max_idx = heapq.heappop(diff_heap)
        perimeters[max_idx] += 2 * math.sqrt(cookies[max_idx][0] * cookies[max_idx][1])