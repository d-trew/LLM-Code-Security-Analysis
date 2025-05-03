from sys import stdin
import bisect as bs

def solve():
    N, K = map(int, input().split())
    P = list(map(float, input().split()))
    
    # Sort the probabilities in descending order.
    P.sort(reverse=True)
    
    max_prob = 0.0
    
    for i in range(K//2):
        # Calculate the probability of a tie.
        prob = (P[i] * P[N-1-i])
        
        if prob > max_prob:
            max_prob = prob
            
    return max_prob
    
T = int(stdin.readline())
for t in range(T):
    print('Case #{}: {}'.format(t+1, solve()))