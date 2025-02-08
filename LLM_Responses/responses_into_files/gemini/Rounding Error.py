def solve():
    N, L = map(int, input().split())
    C = list(map(int, input().split()))
    
    remaining = N - sum(C)
    
    percentages = [(c / N) * 100 for c in C]
    
    
    def round_percentage(p):
        return int(round(p))

    def calculate_total(percentages):
        total = sum(map(round_percentage, percentages))
        return total

    max_sum = 0
    
    
    for i in range(remaining + 1):
        temp_percentages = list(percentages)
        
        
        for j in range(i):
          temp_percentages[j] += (100.0 / N)

        
        for k in range(remaining-i):
            temp_percentages.append(100.0 / N)
            
        max_sum = max(max_sum, calculate_total(temp_percentages))

    return max_sum

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")