def solve():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))

    count = 0
    for L in range(N):
        for R in range(L, N):
            charles_choices = []
            max_charles_skill = -1
            for i in range(L, R + 1):
                if C[i] > max_charles_skill:
                    max_charles_skill = C[i]
                    charles_choices = [i]
                elif C[i] == max_charles_skill:
                    charles_choices.append(i)

            delila_choices = []
            max_delila_skill = -1
            for i in range(L, R + 1):
                if D[i] > max_delila_skill:
                    max_delila_skill = D[i]
                    delila_choices = [i]
                elif D[i] == max_delila_skill:
                    delila_choices.append(i)

            is_fair = False
            for c in charles_choices:
                for d in delila_choices:
                    if abs(C[c] - D[d]) <= K:
                        is_fair = True
                        break
                if is_fair:
                    break
            if is_fair:
                count += 1

    return count

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")