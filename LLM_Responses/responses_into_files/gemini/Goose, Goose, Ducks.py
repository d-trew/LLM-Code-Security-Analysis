def solve():
    N, M, S = map(int, input().split())
    duck_meetings = []
    for _ in range(M):
        duck_meetings.append(list(map(int, input().split())))
    statements = []
    for _ in range(S):
        statements.append(list(map(int, input().split())))

    min_ducks = N

    for i in range(1 << N):
        ducks = []
        geese = []
        for j in range(N):
            if (i >> j) & 1:
                ducks.append(j + 1)
            else:
                geese.append(j + 1)

        if not ducks:
            continue

        feasible = True
        for k in range(S):
            statement = statements[k]
            speaker = statement[0]
            other = statement[1]
            x = statement[2]
            y = statement[3]
            t = statement[4]

            is_goose_statement = speaker in geese

            if is_goose_statement:
                consistent = False
                for duck_meeting in duck_meetings:
                    dx = duck_meeting[0] -x
                    dy = duck_meeting[1]-y
                    dt = duck_meeting[2]-t
                    if dx*dx + dy*dy <= dt*dt:
                        consistent = True
                        break

                if not consistent:
                    feasible = False
                    break

        if feasible:
            min_ducks = min(min_ducks, len(ducks))

    return min_ducks

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")