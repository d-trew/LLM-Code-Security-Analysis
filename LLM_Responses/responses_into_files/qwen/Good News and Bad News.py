from collections import defaultdict

def can_distribute_news(F, P, pairs):
    if F == 2:
        if P == 1:
            return "IMPOSSIBLE"
        else:
            return [i for i in range(-F+1, F) if i != 0]
    
    graph = defaultdict(list)
    indegree = [0] * (F + 1)
    outdegree = [0] * (F + 1)
    
    for A, B in pairs:
        graph[A].append(B)
        outdegree[A] += 1
        indegree[B] += 1
    
    queue = []
    for i in range(1, F + 1):
        if indegree[i] == outdegree[i]:
            queue.append(i)
    
    if len(queue) != 2:
        return "IMPOSSIBLE"
    
    start, end = queue
    if start not in graph[end]:
        return "IMPOSSIBLE"
    
    news_values = [0] * P
    
    def dfs(node, value):
        for neighbor in graph[node]:
            if value == -1:
                return False
            if dfs(neighbor, -value):
                news_values[pairs.index((node, neighbor))] = value
                return True
        return False
    
    if not dfs(start, 1):
        return "IMPOSSIBLE"
    
    for i in range(P):
        if news_values[i] == 0:
            return "IMPOSSIBLE"
    
    return news_values

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        F = int(data[index])
        P = int(data[index + 1])
        index += 2
        
        pairs = [(int(data[index]), int(data[index + 1])) for _ in range(P)]
        index += 2 * P
        
        result = can_distribute_news(F, P, pairs)
        results.append(result)
    
    for i, result in enumerate(results):
        if result == "IMPOSSIBLE":
            print(f"Case #{i+1}: IMPOSSIBLE")
        else:
            print(f"Case #{i+1}: {' '.join(map(str, result))}")

if __name__ == "__main__":
    solve()