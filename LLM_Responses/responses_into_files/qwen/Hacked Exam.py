from fractions import Fraction

def max_expected_score(N, Q, answers):
    from collections import Counter
    
    # Count the frequency of each answer for each question
    count = [Counter() for _ in range(Q)]
    for a, s in answers:
        for i, c in enumerate(a):
            count[i][c] += 1
    
    # Calculate the probability of each answer being correct
    prob = []
    for c in count:
        total = sum(c.values())
        prob.append(Fraction(sum(v * (i if i == 'T' else -i) for i, v in c.items()), total))
    
    # Determine the best sequence of answers
    best_seq = ''.join('T' if p > 0 else 'F' for p in prob)
    expected_score = sum(p * s for p, (_, s) in zip(prob, answers)) / len(answers)
    
    return best_seq, expected_score

def solve():
    T = int(input())
    results = []
    for t in range(1, T + 1):
        N, Q = map(int, input().split())
        answers = [input().split() for _ in range(N)]
        seq, score = max_expected_score(N, Q, answers)
        results.append(f"Case #{t}: {seq} {score.numerator}/{score.denominator}")
    return '\n'.join(results)

print(solve())