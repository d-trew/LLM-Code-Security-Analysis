from itertools import permutations

def count_substrings(s, sub):
    return s.count(sub)

def solve(N, M, prerequisites, cool_words):
    courses = list(range(1, N + 1))
    basic_courses = [i for i in range(1, N + 1) if i not in prerequisites.values()]
    advanced_courses = [i for i in range(1, N + 1) if i in prerequisites.values()]
    
    valid_sequences = []
    for perm in permutations(courses):
        valid = True
        for course in advanced_courses:
            prereq = prerequisites[course]
            if perm.index(course) < perm.index(prereq):
                valid = False
                break
        if valid:
            valid_sequences.append(perm)
    
    results = []
    for cool_word in cool_words:
        count = 0
        for seq in valid_sequences:
            if any(count_substrings(''.join(map(str, seq)), cool_word[:i+1]) > 0 for i in range(len(cool_word))):
                count += 1
        results.append(round(count / len(valid_sequences), 2))
    
    return results

# Read input
T = int(input())
results = []
for t in range(1, T + 1):
    N, M = map(int, input().split())
    prerequisites = {}
    for _ in range(N - 1):
        a, b = map(int, input().split())
        prerequisites[b] = a
    cool_words = [input() for _ in range(M)]
    
    result = solve(N, M, prerequisites, cool_words)
    results.append(f"Case #{t}: {''.join(map(str, result))}")

# Print output
for res in results:
    print(res)