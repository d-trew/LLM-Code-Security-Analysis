def max_fun(N, F, P):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for i in range(1, N + 1):
        if P[i - 1] != 0:
            graph[P[i - 1]].append(i)
    
    def dfs(node):
        visited.add(node)
        fun = F[node - 1]
        for neighbor in graph[node]:
            if neighbor not in visited:
                fun = max(fun, dfs(neighbor))
        return fun
    
    initiators = [i for i in range(1, N + 1) if P[i - 1] == 0]
    max_total_fun = 0
    for initiator in sorted(initiators):
        visited = set()
        chain_reaction_fun = dfs(initiator)
        max_total_fun += chain_reaction_fun
    
    return max_total_fun

def solve():
    T = int(input())
    results = []
    for t in range(1, T + 1):
        N = int(input())
        F = list(map(int, input().split()))
        P = list(map(int, input().split()))
        result = max_fun(N, F, P)
        results.append(f"Case #{t}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()