import sys
from collections import defaultdict

def find_route(buildings, slides):
    visited = [False] * (len(buildings) + 1)
    visited[0] = True
    adjacency_list = {}
    
    for u, v in slides:
        if u not in adjacency_list:
            adjacency_list[u] = [v]
        else:
            adjacency_list[u].append(v)
        
        if v not in adjacency_list:
            adjacency_list[v] = [u]
        else:
            adjacency_list[v].append(u)
    
    stack = [(1, 0)] # start at building 1 and take one step
    while stack:
        node, steps = stack.pop()
        
        if visited[node]:
            continue
        
        visited[node] = True
        if all(visited):
            return steps + 1
        
        for neighbor in adjacency_list.get(node, []):
            stack.append((neighbor, steps + 1))
    
    return "IMPOSSIBLE"

def main():
    T = int(input()) # number of test cases
    for i in range(T):
        B, S = map(int, input().split())
        
        slides = []
        for _ in range(S):
            U, V = map(int, input().split())
            slides.append((U, V))
            
        route_length = find_route([x+1 for x in range(B)], slides)
        
        if route_length == "IMPOSSIBLE":
            print("Case #{}: IMPOSSIBLE".format(i+1))
        else:
            visited = [False] * (len(slides)+1)
            for u, v in slides:
                if not visited[u]:
                    visited[u] = True
                    print("Case #{}: {} 1".format(i+1), end=" ")
                if not visited[v]:
                    visited[v] = True
                    print(v, end=" ")
            print()
        
if __name__ == "__main__":
    main()