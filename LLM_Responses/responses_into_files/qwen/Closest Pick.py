from typing import List

def max_win_probability(N: int, K: int, P: List[int]) -> float:
    P = sorted(P)
    M = len(P)
    
    if M == 0:
        return 1.0
    
    left, right = 0, K - 1
    best_prob = 0.0
    
    while left <= right:
        mid = (left + right) // 2
        
        count_less = sum(1 for p in P if p < mid)
        count_greater = sum(1 for p in P if p > mid)
        
        prob = max(count_less / M, count_greater / M)
        
        best_prob = max(best_prob, prob)
        
        if count_less == count_greater:
            left = mid + 1
        elif count_less < count_greater:
            right = mid - 1
        else:
            left = mid + 1
    
    return best_prob

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        P = list(map(int, data[index + 2:index + 2 + N]))
        index += 2 + N
        
        result = max_win_probability(N, K, P)
        results.append(f"Case #{_+1}: {result:.6f}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()