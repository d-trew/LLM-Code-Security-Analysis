from collections import defaultdict, deque

def find_latencies(T, test_cases):
    results = []
    
    for case_num, (C, D, Xs, connections) in enumerate(test_cases, start=1):
        # Initialize adjacency list and latency dictionary
        adj_list = defaultdict(list)
        latencies = {i: None for i in range(2, C+1)}
        
        # Build the adjacency list
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Initialize queue with source computer and its latency
        queue = deque([(1, 0)])
        visited = {1}
        
        while queue:
            current, time = queue.popleft()
            
            for neighbor in adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    latencies[neighbor] = time + abs(Xs[neighbor-2])
                    queue.append((neighbor, time + abs(Xs[neighbor-2])))
        
        # Sort the connections by their order of appearance
        sorted_connections = sorted(connections, key=lambda x: (x[0], x[1]))
        
        # Assign latencies to each connection
        for u, v in sorted_connections:
            if latencies[u] > latencies[v]:
                latencies[u], latencies[v] = latencies[v], latencies[u]
            
            result = abs(latencies[u] - latencies[v])
            results.append(result)
    
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    C, D = map(int, input().split())
    Xs = list(map(int, input().split()))
    connections = [tuple(map(int, input().split())) for _ in range(D)]
    test_cases.append((C, D, Xs, connections))

# Find and print results
results = find_latencies(T, test_cases)
for i, result in enumerate(results):
    print(f"Case #{i+1}: {result}")