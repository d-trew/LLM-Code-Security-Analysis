T = int(input())
for _ in range(T):
    A = int(input())
    robots = [input() for _ in range(A)]
    win_program = "R" * (len(robots[0]) // 3) + "P"
    if any(len(program) % 3 != 0 or program[:3] == win_program[:3] for program in robots):
        print(f"Case #{_+1}: IMPOSSIBLE")
    else:
        print(f"Case #{_+1}: {win_program}")