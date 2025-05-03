from fractions import Fraction

def calculate_probability(N, K, U, P):
    from itertools import combinations_with_replacement
    
    max_prob = Fraction(0)
    
    for r in range(K, N + 1):
        for combo in combinations_with_replacement(range(N), r):
            prob = Fraction(1)
            remaining_units = U
            
            for i in range(N):
                if i in combo:
                    if remaining_units > 0:
                        p_i = min(P[i] + Fraction(remaining_units, N - len(combo) + 1), Fraction(1))
                        prob *= p_i
                        remaining_units -= (P[i] - p_i).numerator * (N - len(combo) + 1)
                    else:
                        prob *= P[i]
                else:
                    prob *= (1 - P[i])
            
            max_prob = max(max_prob, prob)
    
    return max_prob

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for t in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        U = Fraction(data[index + 2])
        P = [Fraction(data[index + 3 + i]) for i in range(N)]
        
        result = calculate_probability(N, K, U, P)
        print(f"Case #{t+1}: {result}")

if __name__ == "__main__":
    main()