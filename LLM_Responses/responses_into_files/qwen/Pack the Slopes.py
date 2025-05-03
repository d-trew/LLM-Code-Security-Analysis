import sys

def max_skiers_and_min_expense(N, slopes):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    capacity = [0] * (N + 1)
    cost = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    
    for u, v, s, c in slopes:
        graph[u].append(v)
        graph[v].append(u)
        capacity[u][v] = s
        capacity[v][u] = s
        cost[u][v] = c
        cost[v][u] = -c
    
    def bfs():
        parent = [-1] * (N + 1)
        distance = [float('inf')] * (N + 1)
        distance[1] = 0
        
        queue = deque([1])
        
        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                if distance[v] == float('inf') and capacity[u][v] > 0:
                    parent[v] = u
                    distance[v] = distance[u] + cost[u][v]
                    queue.append(v)
        
        return parent, distance
    
    max_skiers = 0
    min_expense = 0
    
    while True:
        parent, distance = bfs()
        if parent[N] == -1:
            break
        
        path_flow = float('inf')
        s = N
        
        while s != 1:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        max_skiers += path_flow
        min_expense += path_flow * distance[N]
        
        v = N
        while v != 1:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
    
    return max_skiers, min_expense

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        
        slopes = []
        
        for _ in range(N - 1):
            u = int(data[index])
            v = int(data[index + 1])
            s = int(data[index + 2])
            c = int(data[index + 3])
            index += 4
            slopes.append((u, v, s, c))
        
        max_skiers, min_expense = max_skiers_and_min_expense(N, slopes)
        results.append(f"Case #{_ + 1}: {max_skiers} {min_expense}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()