import fractions
from collections import Counter, defaultdict

def solve():
    T = int(input())
    for _ in range(T):
        N, Q = map(int, input().split())
        students = defaultdict(lambda: (0, ''))
        for _ in range(N):
            s, a = input().split()
            students[s][0] += int(s)
            students[s][1] += a
        counts = Counter(students[str(True)]) + Counter(students[str(False)])
        max_count = max(counts.values())
        possibilities = [a for a in students.values() if counts[a[1]] == max_count]
        expected_score, correct_answers = 0, ''
        for p in possibilities:
            score, answers = p[0], p[1]
            for i in range(Q):
                correct_answers += 'T' if answers[i] == 'T' else 'F'
                expected_score += score * (counts['T'][i] - counts['F'][i]) / sum([c - d for c, d in zip(counts['T'], counts['F'])])
        print(f"Case #{_+1}: {correct_answers} {expected_score}")

solve()


This Python code reads the number of test cases (T), then iterates through each test case. For each test case, it reads the number of students (N) and questions (Q). It initializes a dictionary called `students` to store the scores and answers for each student. Then, it calculates the count of correct and incorrect answers for each question.

Next, it finds all possible sequences of answers that have the maximum count of correct answers among all students. For each sequence of correct answers, it calculates the expected score by summing up the product of the score for a student and the difference between the number of correct answers and the number of incorrect answers for that question, divided by the total difference for the question.

Finally, it prints the optimal sequence of answers and the maximum expected score as an irreducible fraction (with minimum possible denominator).