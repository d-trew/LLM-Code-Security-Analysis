from itertools import combinations

def max_tie_probability(N, K, probabilities):
    max_prob = 0
    for committee in combinations(probabilities, K):
        yes_prob = sum(committee)
        no_prob = 1 - yes_prob
        tie_prob = yes_prob * no_prob + no_prob * yes_prob
        if tie_prob > max_prob:
            max_prob = tie_prob
    return max_prob

T = int(input())
results = []
for i in range(1, T + 1):
    N, K = map(int, input().split())
    probabilities = list(map(float, input().split()))
    results.append((i, max_tie_probability(N, K, probabilities)))

for case_num, prob in results:
    print(f"Case #{case_num}: {prob:.6f}")