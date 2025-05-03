def count_fair_duels(N, K, C, D):
    # Initialize the count of fair duels to zero
    count = 0
    
    # Iterate over all possible ranges (L, R)
    for L in range(1, N+1):
        maxC = max((C[i] if L <= i + 1 <= R else 0) for R in range(1, N+1))
        minD = min((D[i] if L <= i + 1 <= R else float('inf')) for R in range(N+1))
        
        # If the difference between maxC and minD is at most K, increment count
        if maxC - minD <= K:
            count += 1
    
    return count