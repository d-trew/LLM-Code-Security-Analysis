def find_parade_route(T):
    results = []
    
    for t in range(1, T + 1):
        B, S = map(int, input().split())
        graph = [[] for _ in range(B)]
        
        for _ in range(S):
            U_i, V_i = map(int, input().split())
            graph[U_i - 1].append(V_i - 1)
        
        def dfs(node, path):
            if len(path) > 10**6:
                return False
            if node == 0 and len(path) != B * 2 + 1:
                return False
            if node == 0 and len(path) == B * 2 + 1:
                results.append((t, path))
                return True
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, path + [neighbor])
            visited[node] = False
        
        visited = [False] * B
        dfs(0, [0])
    
    for case, route in results:
        print(f"Case #{case}: {len(route)}")
        print(" ".join(map(str, route)))

# Example usage:
T = int(input())
find_parade_route(T)