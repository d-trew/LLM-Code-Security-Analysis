from math import comb
T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    cool_words = [input().upper() for _ in range(M)]
    prerequisites = {}
    for i in range(N):
        prereq, course = input().split()
        if len(prereq) > 1:
            prerequisites[course] = prereq
    sequences = set()
    def dfs(course, path):
        if course not in prerequisites:
            sequences.add(''.join([c[0] for c in path]))
        else:
            for c in prerequisites[course]:
                dfs(c, path + [(course, c)])
    dfs('C', [])
    answers = []
    for cool_word in cool_words:
        count = 0
        for seq in sequences:
            if cool_word in seq:
                count += 1
        answers.append(f'{count/len(sequences):.4f}')
    print('Case #{}: {}'.format(_, ' '.join(answers)))