T = int(input())
for i in range(1, T+1):
    N = int(input())
    graph = {}
    for _ in range(N-1):
        u, v, s, c = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, s, c))
        graph[v].append((u, 0, -c)) # add reverse edge
    max_skiers = 1
    min_expense = float('inf')
    for _ in range(N):
        skiers = [0] * (N+1)
        expense = 0
        for i in range(1, N):
            if graph[i]:
                slope = min((v, s, c) for v, s, c in graph[i])
                graph[i].remove(slope)
                skiers[slope[0]] += slope[1]
                expense += slope[2] * slope[1]
        max_skiers = max(max_skiers, sum(skiers))
        min_expense = min(min_expense, expense)
    print(f"Case #{i}: {max_skiers} {min_expense}")