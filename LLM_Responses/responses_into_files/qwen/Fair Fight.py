def count_fair_fights(T, test_cases):
    results = []
    
    for i in range(T):
        N, K = map(int, test_cases[i][0].split())
        C = list(map(int, test_cases[i][1].split()))
        D = list(map(int, test_cases[i][2].split()))
        
        fair_count = 0
        
        for L in range(1, N + 1):
            for R in range(L, N + 1):
                charles_best = max(C[L-1:R])
                delila_best = max(D[L-1:R])
                
                if abs(charles_best - delila_best) <= K:
                    fair_count += 1
        
        results.append(f"Case #{i+1}: {fair_count}")
    
    return results

# Example usage:
T = 5
test_cases = [
    ("4 2", "10 20 30 40", "10 10 10 10"),
    ("3 1", "7 8 9", "6 7 8"),
    ("1 0", "5", "5"),
    ("4 5", "1 2 3 4", "4 3 2 1"),
    ("5 1", "10 20 30 40 50", "50 40 30 20 10")
]

results = count_fair_fights(T, test_cases)
for result in results:
    print(result)