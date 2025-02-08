import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve():
    N, Q = map(int, input().split())
    students = []
    for _ in range(N):
        line = input().split()
        students.append((line[0], int(line[1])))

    possible_answers = []
    for i in range(2**Q):
        answer = bin(i)[2:].zfill(Q).replace('0', 'F').replace('1', 'T')
        valid = True
        for student_answers, student_score in students:
            score = 0
            for j in range(Q):
                if student_answers[j] == answer[j]:
                    score += 1
            if score != student_score:
                valid = False
                break
        if valid:
            possible_answers.append(answer)

    if len(possible_answers) == 0:
        return "Error: No consistent answers found."

    best_answer = ""
    max_expected_score_num = 0
    max_expected_score_den = 1

    if len(possible_answers) == 1:
        best_answer = possible_answers[0]
        max_expected_score_num = sum(1 for i in range(Q) if possible_answers[0][i] == 'T')
        max_expected_score_den = 1

    else:
        best_answer = possible_answers[0]
        max_expected_score_num = 0
        max_expected_score_den = len(possible_answers)
        for i in range(Q):
            count_t = 0
            for ans in possible_answers:
                if ans[i] == 'T':
                    count_t +=1
            max_expected_score_num += max(count_t, len(possible_answers) - count_t)


    common_divisor = gcd(max_expected_score_num, max_expected_score_den)
    return f"{best_answer} {max_expected_score_num // common_divisor}/{max_expected_score_den // common_divisor}"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")