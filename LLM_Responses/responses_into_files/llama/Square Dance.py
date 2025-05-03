T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    skill_levels = [list(map(int, input().split())) for _ in range(R)]
    eliminated = set()
    round_interest = 0
    rounds = 1
    while True:
        interest = sum(skill_levels[i][j] for i in range(R) for j in range(C) if (i, j) not in eliminated)
        eliminated = {(i, j) for i in range(R) for j in range(C) if any(neighbor in eliminated or neighbor[0] == i or neighbor[1] == j for neighbor in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)])}
        round_interest += interest
        rounds += 1
        if not eliminated:
            break
    print(f"Case #{_+1}: {round_interest}")