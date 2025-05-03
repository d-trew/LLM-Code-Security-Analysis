def max_lead(metals, inventory):
    from collections import defaultdict
    
    # Create a graph where each node is a metal and edges represent the formulas
    graph = defaultdict(list)
    for i in range(1, len(metals)):
        r1, r2 = metals[i]
        graph[r1].append((r2, 1))
        graph[r2].append((r1, 1))
    
    # Use a dictionary to store the inventory
    inv = {i: inventory[i] for i in range(1, len(metals))}
    
    # Function to perform DFS and find the maximum lead that can be produced from metal i
    def dfs(i):
        if i == 1:
            return inv[1]
        max_lead_from_i = 0
        for j, weight in graph[i]:
            if inv[j] >= weight:
                inv[j] -= weight
                max_lead_from_i = max(max_lead_from_i, dfs(j) + weight)
                inv[j] += weight
        return max_lead_from_i
    
    # Calculate the maximum lead for each test case
    results = []
    for i in range(len(metals)):
        max_lead = dfs(i)
        results.append(f"Case #{i+1}: {max_lead}")
    
    return results

# Read input and process each test case
T = int(input())
results = []
for _ in range(T):
    M = int(input())
    metals = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(M)]
    inventory = list(map(int, input().split()))
    results.extend(max_lead(metals, inventory))

# Print the results
for result in results:
    print(result)