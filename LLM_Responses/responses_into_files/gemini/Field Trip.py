def solve():
    N = int(input())
    positions = []
    for _ in range(N):
        positions.append(list(map(int, input().split())))

    min_turns = float('inf')

    for r in range(100): # Adjust range as needed for larger inputs
        for c in range(100):
            max_kid_turns = 0
            for i in range(N):
                kid_turns = max(abs(positions[i][0] - r), abs(positions[i][1] - c))
                max_kid_turns = max(max_kid_turns, kid_turns)
            
            teacher_turns = max(abs(positions[0][0] - r), abs(positions[0][1]-c))
            min_turns = min(min_turns, max(max_kid_turns, teacher_turns))

    return min_turns


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")