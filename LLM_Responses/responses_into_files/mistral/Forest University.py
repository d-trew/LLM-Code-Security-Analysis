import re
from collections import Counter
import fractions

def get_courses(input_str):
    courses = input_str.split('\n')[1:]
    return [course.strip() for course in courses]

def get_prerequisites(input_str):
    prerequisites = {}
    for line in input_str.split('\n')[2:-1]:
        course, prereq = line.split(': ')
        prerequisites[course] = [prereq.strip()] if ',' not in prereq else prereq.strip().split(', ')
    return prerequisites

def valid_sequences(courses, prerequisites):
    sequences = []

    def dfs(remaining, taken=[]):
        if not remaining:
            sequences.append(taken)
            return

        course = remaining[0]
        for p in prerequisites[course]:
            new_remaining = [r for r in remaining if r != p]
            dfs(new_remaining, taken + [course])
        dfs(remaining[1:], taken)

    dfs([c for c in courses if 'prerequisites' not in prerequisites[c]], [])
    return sequences

def cool_words(courses, sequences):
    cool_words = input_str.split('\n')[-1].split(', ')
    word_counts = Counter()
    for sequence in sequences:
        hat = ''.join([course[0] for course in sequence])
        word_counts.update(re.findall('[' + '|'.join(cool_words) + ']', hat))
    return [word_counts[cool_word]/len(sequences) if cool_word in word_counts else 0 for cool_word in cool_words]

def solve(input_str):
    courses = get_courses(input_str)
    prerequisites = get_prerequisites(input_str)
    sequences = valid_sequences(courses, prerequisites)
    return ['Case #{}: {}'.format(i+1, ', '.join(map(str, cool_words(courses, sequences))) for i, cool_word in enumerate([''.join(sorted(cool_words))] + cool_words)) if sequences else ['Case #{}: Error'.format(i+1)])

if __name__ == '__main__':
    import sys
    from timeit import default_timer as timer

    cases = int(input())
    for _ in range(cases):
        input_str = input()
        start = timer()
        result = solve(input_str)
        end = timer()
        print('Case #{}: {}'.format(_+1, ', '.join(map(str, result)))


This Python code reads the input from standard input and solves the described problem. The solution is printed to standard output with the correct format as specified in the description.