from collections import defaultdict

def min_hours_to_complete_tours(camps, tours):
    graph = defaultdict(list)
    
    for i in range(len(tours)):
        start_camp = (i + 1) // 2
        end_camp, leave_time, duration = tours[i]
        graph[start_camp].append((end_camp, leave_time, duration))
    
    def dfs(current_camp, current_time):
        if len(visited) == 2 * camps - 1:
            return (current_time + 23) % 24
        
        min_time = float('inf')
        for end_camp, leave_time, duration in graph[current_camp]:
            if end_camp not in visited and current_time >= leave_time:
                visited.add(end_camp)
                time_to_next_tour = (leave_time - current_time + 23) % 24
                min_time = min(min_time, time_to_next_tour + dfs(end_camp, (current_time + duration) % 24))
                visited.remove(end_camp)
        
        return min_time
    
    visited = {1}
    total_hours = dfs(1, 0)
    
    return total_hours

# Read input
import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
index = 1
results = []

for _ in range(T):
    camps = int(data[index])
    index += 1
    tours = []
    for i in range(2 * camps):
        end_camp = int(data[index]) - 1
        leave_time = int(data[index + 1])
        duration = int(data[index + 2])
        tours.append((end_camp, leave_time, duration))
        index += 3
    
    min_hours = min_hours_to_complete_tours(camps, tours)
    results.append(f"Case #{_+1}: {min_hours}")

# Output results
for result in results:
    print(result)