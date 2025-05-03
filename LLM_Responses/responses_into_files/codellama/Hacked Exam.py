import math

def get_expected_score(answers, scores):
    num_questions = len(answers[0])
    num_students = len(scores)
    expected_score = 0
    for i in range(num_students):
        student_score = 0
        for j in range(num_questions):
            if answers[i][j] == 'T':
                student_score += scores[i][j]
        expected_score += student_score / num_students
    return expected_score

def get_best_answers(scores, num_questions, num_students):
    best_answers = []
    for i in range(num_students):
        best_answer = ''
        max_score = -1
        for j in range(num_questions):
            if scores[i][j] > max_score:
                max_score = scores[i][j]
                best_answer = 'T' * max_score + 'F' * (num_questions - max_score)
        best_answers.append(best_answer)
    return best_answers

def solve(scores):
    num_students, num_questions = scores[0]
    answers = []
    for i in range(1, len(scores)):
        answers.append(list(scores[i][2]))
    expected_score = get_expected_score(answers, scores)
    best_answers = get_best_answers(scores, num_questions, num_students)
    return (expected_score, best_answers)

def main():
    test_cases = int(input())
    for i in range(test_cases):
        scores = []
        for _ in range(int(input())):
            scores.append(list(map(int, input().split())))
        expected_score, best_answers = solve(scores)
        print("Case #" + str(i+1) + ": " + str(expected_score) + " " + str(best_answers))

if __name__ == '__main__':
    main()