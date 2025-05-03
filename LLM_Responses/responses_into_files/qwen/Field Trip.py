T = int(input())
for t in range(1, T + 1):
    N = int(input())
    people = []
    for _ in range(N):
        r, c = map(int, input().split())
        people.append((r, c))
    min_turns = float('inf')
    for i in range(N):
        turns = 0
        teacher_r, teacher_c = people[i]
        for j in range(i + 1, N):
            if (teacher_r, teacher_c) != people[j]:
                dr, dc = abs(people[j][0] - teacher_r), abs(people[j][1] - teacher_c)
                turns += max(dr, dc)
        min_turns = min(min_turns, turns)
    print(f"Case #{t}: {min_turns}")