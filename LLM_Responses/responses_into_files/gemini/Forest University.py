def solve():
    N = int(input())
    prerequisites = {}
    courses = {}
    for i in range(N):
        line = input().split()
        course_name = line[0]
        courses[course_name] = i
        if len(line) > 1:
            prerequisites[course_name] = line[1]

    M = int(input())
    cool_words = [input() for _ in range(M)]

    
    def get_valid_sequences(current_sequence, taken_courses):
        if len(taken_courses) == N:
            return [current_sequence]

        valid_sequences = []
        for course_name in courses:
            if course_name not in taken_courses:
                can_take = True
                if course_name in prerequisites:
                    if prerequisites[course_name] not in taken_courses:
                        can_take = False
                if can_take:
                    new_sequence = current_sequence + course_name[0]
                    valid_sequences.extend(get_valid_sequences(new_sequence, taken_courses | {course_name}))
        return valid_sequences

    
    all_sequences = get_valid_sequences("", set())
    
    results = []
    for word in cool_words:
        count = 0
        for seq in all_sequences:
            if word in seq:
                count += 1
        results.append(count / len(all_sequences) if len(all_sequences) > 0 else 0)
    return " ".join(map(str, results))

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")