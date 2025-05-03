def max_score(S):
    S = list(map(lambda x: True if x == 'C' else False, S))  # Convert to boolean values
    assistant_mood = [True] + S[:-1]  # Create a shifted version of the moods for comparison
    problem_sets = []
    total = 0
    
    for day in range(len(S)):
        if (day % 2 == 0):  # Request a set on even days
            problem_set = S[day] == assistant_mood[day]
            problem_sets.append((problem_set, day))
        else:  # Submit the most recent requested set on odd days
            if not problem_sets:
                continue
            points = 10 if problem_sets[-1][0] == S[day] == assistant_mood[day] else 5
            total += min(points, 10)
            problem_sets.pop()
    
    return total

T = int(input().strip())
for t in range(T):
    S = input().strip()
    print("Case #{}: {}".format(t+1, max_score(S)))