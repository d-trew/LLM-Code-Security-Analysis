import sys
from operator import itemgetter

def solve():
    _, n, k = map(int, input().split())
    u = float(input())
    ps = list(map(float, input().split()))
    
    if len(ps) != n: return "Error: Incorrect number of core probabilities"
    
    # Calculate the probability for each core to function properly after training
    p_train = [min(1.0, p + u / (n - 1)) if i < n - 1 else min(1.0, p + u / n) for i, p in enumerate(ps)]
    
    # Sort the cores by their training probabilities in descending order
    sorted_cores = sorted([(p, i) for i, p in enumerate(p_train)], reverse=True)
    
    # Assign units to the top k cores with highest success probability
    total_units = u
    for i in range(k):
        p, _ = sorted_cores[i]
        if i < n - 1: total_units -= (1.0 - p) / (n - 1)
        else: total_units -= 1.0 - p
    
    # Assign remaining units to the next core with highest success probability
    if k < n:
        p, _ = sorted_cores[k]
        if k < n - 1: p = min(p, (1.0 - total_units) / (n - 1))
        else: p = 1.0 - total_units
    
    # Calculate the final probability that the AI will function properly
    prob = 1.0
    for i in range(k):
        p, _ = sorted_cores[i]
        if i < k - 1: prob *= (1.0 - min(p, 1.0))
        else: prob *= 1.0 - min(p, 1.0)
    
    return prob

def main():
    t = int(input())
    for i in range(1, t + 1):
        print("Case #{}: {}".format(i, solve()))

if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    main()