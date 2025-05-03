def bathroom_stalls(N, K):
    if N == K or N == 1:
        return (0, 1)
    
    occupied = [False]*(N+2)
    LS, RS = [0]*K, [0]*K
    leftmost_empty = 1
    rightmost_empty = N
    
    for i in range(K):
        if not occupied[leftmost_empty]:
            occupied[leftmost_empty] = True
            LS[i] = leftmost_empty - 1
            RS[i] = rightmost_empty + 1 - leftmost_empty - 2
            
            while occupied[rightmost_empty]:
                rightmost_empty -= 1
                
        else:
            occupied[rightmost_empty] = True
            LS[i] = rightmost_empty - 1
            RS[i] = leftmost_empty + 2 - rightmost_empty - 1
            
            while occupied[leftmost_empty]:
                leftmost_empty += 1
                
    return (max(LS), min(RS))

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    max_ls_rs = bathroom_stalls(N, K)
    print("Case #{}: {} {}".format(t, *max_ls_rs))