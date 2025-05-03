Here's the Python code that solves this problem using Breadth-First Search (BFS):


from collections import deque

def binary_transform(S, E):
    visited = set()
    queue = deque([(S, 0)])
    
    while queue:
        curr, step = queue.popleft()
        
        if curr == E:
            return step
            
        for next in (int(curr) ^ int('1'*len(curr), 2)), int(curr)*2:
            if next not in visited and '0'+bin(next)[2:] not in visited:
                queue.append((bin(next)[2:].zfill(8), step+1))
                visited.add('0'+bin(next)[2:])
                
        for next in int(curr) ^ int('1'*len(curr), 2):
            if '1'+bin(next)[2:] not in visited and int(curr) ^ int('1'*len(curr), 2) not in visited:
                queue.append(('1'+bin(next)[2:].zfill(8), step+1))
                visited.add('1'+bin(next)[2:])
                
    return "IMPOSSIBLE"

T = int(input())
for t in range(1, T+1):
    S, E = input().split()
    print("Case #{}: {}".format(t, binary_transform(S, E)))

This code uses a deque for BFS and a set to keep track of visited nodes. It starts from the initial number `S` and tries all possible transformations (double operation or NOT operation) in each step until it reaches the target number `E`. The function returns the minimum number of operations needed, or "IMPOSSIBLE" if no such transformation is possible.