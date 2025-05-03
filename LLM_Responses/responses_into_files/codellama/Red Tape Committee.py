import math

def get_tie_probability(N, K, P):
    # Calculate the probability of a tie for each possible committee size
    tie_probs = []
    for i in range(K+1):
        prob = 0
        for j in range(i):
            prob += math.comb(N, i) * (P[j] * P[i-j])
        tie_probs.append(prob)
    
    # Find the maximum probability of a tie
    max_tie_prob = max(tie_probs)
    
    return max_tie_prob

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        P = [float(x) for x in input().split()]
        print("Case #" + str(t+1) + ": " + str(get_tie_probability(N, K, P)))