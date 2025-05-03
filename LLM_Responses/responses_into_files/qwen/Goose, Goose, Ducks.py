from collections import defaultdict

def min_ducks(T, test_cases):
    results = []
    
    for i in range(T):
        N, M, S = map(int, input().split())
        duck_meetings = [tuple(map(int, input().split())) for _ in range(M)]
        statements = [tuple(map(int, input().split())) for _ in range(S)]
        
        # Create a graph to represent the possible paths
        graph = defaultdict(list)
        for A, B, U, V, D in statements:
            graph[A].append((B, U, V, D))
            graph[B].append((A, U, V, D))
        
        # Perform BFS to find the minimum number of ducks
        from collections import deque
        
        def bfs(start):
            visited = set()
            queue = deque([(start, 0)])
            while queue:
                current, time = queue.popleft()
                if time >= D and (current, U, V) not in visited:
                    visited.add((current, U, V))
                    continue
                for neighbor, U2, V2, D2 in graph[current]:
                    if (neighbor, U2, V2) not in visited:
                        queue.append((neighbor, time + 1))
            return len(visited)
        
        min_ducks = float('inf')
        for A in range(1, N+1):
            min_ducks = min(min_ducks, bfs(A))
        
        results.append(f"Case #{i+1}: {min_ducks}")
    
    return results

# Read input
T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(int(input()))
    N, M, S = map(int, input().split())
    duck_meetings = [tuple(map(int, input().split())) for _ in range(M)]
    statements = [tuple(map(int, input().split())) for _ in range(S)]
    test_cases.extend([N, M, S] + duck_meetings + statements)

# Process the input and print results
results = min_ducks(T, test_cases)
for result in results:
    print(result)