def max_groups(N, P, G):
    # Sort group sizes in decreasing order
    G.sort(reverse=True)
    
    leftovers = 0
    fresh_groups = N
    
    for i in range(N):
        total_pieces = G[i] + leftovers
        
        # Calculate number of packs needed and remaining pieces
        packs, leftovers = divmod(total_pieces, P)
        
        if packs == 0:
            fresh_groups -= 1
            
    return fresh_groups

T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())
    G = list(map(int, input().split()))
    
    print("Case #{}: {}".format(t, max_groups(N, P, G)))