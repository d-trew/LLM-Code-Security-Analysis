MOD = 10**9 + 7

def max_lead(M, R, G):
    if 1 in R:
        return 'UNBOUNDED'
    
    graph = [[] for _ in range(M+1)]
    in_degree = [0] * (M+1)
    
    for i in range(1, M+1):
        if R[i-1] != i:
            graph[R[i-1]].append(i)
            in_degree[i] += 1
    
    queue = []
    for i in range(2, M+1):
        if in_degree[i] == 0:
            queue.append(i)
    
    lead = [G[0]]
    while queue:
        current = queue.pop()
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            lead[neighbor-1] = (lead[neighbor-1] + G[current-1]) % MOD
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return str(max(lead))

def solve():
    T = int(input())
    for t in range(1, T+1):
        M = int(input())
        R = [int(x) for x in input().split()]
        G = [int(x) for x in input().split()]
        result = max_lead(M, R, G)
        print(f"Case #{t}: {result}")

if __name__ == "__main__":
    solve()