def solve():
    N = int(input())
    P = list(map(int, input().split()))

    parties = [chr(ord('A') + i) for i in range(N)]
    senators = {}
    for i in range(N):
        senators[parties[i]] = P[i]

    plan = []
    while sum(senators.values()) > 0:
        max_party = ""
        max_count = 0
        for party, count in senators.items():
            if count > max_count:
                max_count = count
                max_party = party

        if max_count <= sum(senators.values()) // 2:
            if senators[max_party] > 0:
                plan.append(max_party)
                senators[max_party] -= 1

        else:
            second_max_party = ""
            second_max_count = 0
            for party, count in senators.items():
                if party != max_party and count > second_max_count:
                    second_max_count = count
                    second_max_party = party
            
            if senators[max_party] > 0 and senators[second_max_party] > 0:
                plan.append(max_party + second_max_party)
                senators[max_party] -= 1
                senators[second_max_party] -=1
            elif senators[max_party] > 0:
                plan.append(max_party)
                senators[max_party] -= 1


    return " ".join(plan)

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")