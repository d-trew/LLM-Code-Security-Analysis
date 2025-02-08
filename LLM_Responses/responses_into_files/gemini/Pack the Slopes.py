def solve():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        U, V, S, C = map(int, input().split())
        edges.append((U, V, S, C))

    graph = {i: [] for i in range(1, N + 1)}
    for U, V, S, C in edges:
        graph[U].append((V, S, C))

    max_skiers = float('inf')
    min_expense = 0

    
    def dfs(node, path, skiers_count, current_expense):
        nonlocal max_skiers, min_expense

        is_leaf = True
        for neighbor, capacity, cost in graph[node]:
            is_leaf = False
            num_skiers = min(skiers_count, capacity)
            
            new_expense = current_expense + num_skiers * cost
            
            dfs(neighbor, path + [(node, neighbor, num_skiers, cost)], num_skiers, new_expense)

        if is_leaf and node !=1:
            if skiers_count < max_skiers:
                max_skiers = skiers_count
                min_expense = current_expense
            elif skiers_count == max_skiers:
                min_expense = min(min_expense, current_expense)

    dfs(1, [], float('inf'), 0)
    
    return max_skiers, min_expense


T = int(input())
for i in range(1, T + 1):
    max_s, min_e = solve()
    print(f"Case #{i}: {max_s} {min_e}")