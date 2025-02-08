def solve():
    N = int(input())
    activities = []
    for _ in range(N):
        S, E = map(int, input().split())
        activities.append((S, E))

    for i in range(2**N):
        cameron = []
        jamie = []
        assignment = ""
        for j in range(N):
            if (i >> j) & 1:
                cameron.append(activities[j])
                assignment += "C"
            else:
                jamie.append(activities[j])
                assignment += "J"

        valid = True
        for k in range(len(cameron)):
            for l in range(k + 1, len(cameron)):
                if max(cameron[k][0], cameron[l][0]) < min(cameron[k][1], cameron[l][1]):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            for k in range(len(jamie)):
                for l in range(k + 1, len(jamie)):
                    if max(jamie[k][0], jamie[l][0]) < min(jamie[k][1], jamie[l][1]):
                        valid = False
                        break
                if not valid:
                    break

        if valid:
            return assignment

    return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")