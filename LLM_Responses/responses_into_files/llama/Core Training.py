import math

def calculate_probability():
    T = int(input())
    results = []
    
    for _ in range(T):
        N, K = map(int, input().split())
        U = float(input())
        
        P = list(map(float, input().split()))
        
        P.sort(reverse=True)
        used_units = 0
        
        for i in range(N):
            if used_units + (1 - P[i]) > U:
                break
            used_units += 1
        
        probability = 1
        for i in range(K-1, N):
            probability *= P[i]
        
        results.append(f"Case # {_+1}: {probability:.6f}")
    
    print('\n'.join(results))