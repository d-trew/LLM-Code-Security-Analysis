# Read input for T test cases
T = int(input())
for i in range(T):
    # Read N for this case
    N = int(input())
    
    # Generate tree edges
    tree_edges = []
    for j in range(N-1):
        tree_edges.append((j+2, j+1))
        
    # Output tree edges
    print(N-1)
    for edge in tree_edges:
        print(*edge)
    
    # Read M games to play on this tree
    M = int(input())
    
    # Play M games
    game_count = 0
    while game_count < M and True:
        # Ueli's turn
        K = int(input())
        
        if K != N-1:
            print(-1)
            break
        
        A = list(map(int, input().split()))
        for a in A[1:]:
            if a not in tree_edges and (a,A[0]) not in tree_edges:
                print(-1)
                break
            
        # Vreni's turn - always choose the first vertex
        print(N-2)
        print(1)
        
        for j in range(2, N):
            if (j, 1) not in tree_edges and (1,j) not in tree_edges:
                print(-1)
                break
            
        # Check if all vertices are red after Vreni's turn
        is_red = [False]*N
        is_red[0] = True
        for a in A[1:]:
            is_red[a-1] = True
        
        for edge in tree_edges:
            if not (is_red[edge[0]-1] and is_red[edge[1]-1]):
                break
        else:
            game_count += 1