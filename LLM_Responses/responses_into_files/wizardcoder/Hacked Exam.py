import fractions
from collections import Counter

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def get_gcd_lcm(scores):
    gcd_value = 1
    lcm_value = 1
    for score in scores:
        gcd_value = gcd(gcd_value, score[0])
        lcm_value = lcm(lcm_value, score[1])
    return (gcd_value, lcm_value)

def get_expected_score(answers, scores):
    correct_answers = [char for char in answers if char == 'T']
    expected_score = len(correct_answers) / sum([1 for score in scores if score[0] >= len(correct_answers)])
    return expected_score

def main():
    T = int(input())
    for i in range(1, T + 1):
        N, Q = map(int, input().split())
        students = []
        for _ in range(N):
            A, S = input(), int(input())
            students.append((A, S))
        
        scores = [Counter([student[0][i] for student in students]) for i in range(Q)]
        
        gcd_value, lcm_value = get_gcd_lcm(scores)
        expected_score = 0
        for score in scores:
            expected_score += int((score['T'] * lcm_value / gcd_value) * (Q - sum(score.values())) + len(correct_answers))
        
        print("Case #%d: %s %s/%s" % (i, ''.join(['T' for _ in range(expected_score)]), lcm_value // gcd_value) if expected_score >= 0 else "Case #%d: impossible" % i)

if __name__ == "__main__":
    main()