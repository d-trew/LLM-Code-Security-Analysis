import heapq
from collections import defaultdict

def solve(camps, tours):
    graph = defaultdict(list)
    for ei, li, di in tours:
        graph[ei].append((li + di, ei))
    
    _, total_time = heapq.heappop(graph[1])
    visited = {1}
    queue = [(total_time, 1)]
    
    while len(visited) < camps:
        time, start = heapq.heappop(queue)
        
        for end_time, end in graph[start]:
            if end not in visited:
                visited.add(end)
                total_time += (end_time - time + 24) % 24
                queue.append((end_time, end))
                
    return total_time

T = int(input())
for case in range(1, T+1):
    camps = int(input())
    tours = [tuple(map(int, input().split())) for _ in range(2*camps)]
    
    print("Case #{}: {}".format(case, solve(camps, sorted(tours))))