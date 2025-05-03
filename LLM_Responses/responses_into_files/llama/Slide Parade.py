from collections import deque

def gooli_parade(B, S):
    graph = [[] for _ in range(B+1)]
    for i in range(S):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    visited = [[False] * (B + 1) for _ in range(2 ** B)]
    queue = deque([(1, 0)])
    visited[0][1] = True
    
    while queue:
        state, building = queue.popleft()
        if building == B:
            return state
        
        for next_building in graph[building]:
            new_state = state ^ (1 << next_building)
            if not visited[new_state][next_building]:
                visited[new_state][next_building] = True
                queue.append((new_state, next_building))
    
    return 'IMPOSSIBLE'

T = int(input())
for i in range(T):
    B, S = map(int, input().split())
    print(f"Case #{i+1}: {gooli_parade(B, S)}")