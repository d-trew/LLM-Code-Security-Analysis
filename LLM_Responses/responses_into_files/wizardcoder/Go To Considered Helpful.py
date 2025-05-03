import sys
from collections import deque

def get_input():
    T = int(sys.stdin.readline().strip())
    for i in range(1, T+1):
        R, C = map(int, input().split())
        matrix = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
        M_pos = None
        N_pos = None
        
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 'M':
                    M_pos = (r, c)
                elif matrix[r][c] == 'N':
                    N_pos = (r, c)
        
        if not M_pos or not N_pos:
            print(f"Case #{i}: IMPOSSIBLE")
        else:
            bfs(M_pos, N_pos, R, C, matrix)

def bfs(start, end, R, C, matrix):
    queue = deque([((start, 0)])
    visited = set()
    
    while queue:
        pos, depth = queue.popleft()
        
        if pos == end:
            print(f"Case #{i}: {depth}")
            return
        
        if pos in visited:
            continue
            
        visited.add(pos)
        
        for neighbor in get_neighbors(pos, R, C, matrix):
            queue.append((neighbor, depth+1))
    
    print(f"Case #{i}: IMPOSSIBLE")

def get_neighbors(pos, R, C, matrix):
    r, c = pos
    neighbors = []
    
    if r > 0 and matrix[r-1][c] != '#':
        neighbors.append((r-1, c))
        
    if r < R-1 and matrix[r+1][c] != '#':
        neighbors.append((r+1, c)
    
    if c > 0 and matrix[r][c-1] != '#':
        neighbors.append((r, c-1))
        
    if c < C-1 and matrix[r][c+1] != '#':
        neighbors.append((r, c+1)
    
    return neighbors

get_input()