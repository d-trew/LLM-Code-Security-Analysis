T = int(input())
for _ in range(T):
    M = int(input())
    formulas = {}
    for _ in range(M):
        R1, R2 = map(int, input().split())
        if R1 not in formulas:
            formulas[R1] = []
        if R2 not in formulas:
            formulas[R2] = []
        formulas[R1].append(R2)
        formulas[R2].append(1)  # lead is always produced
    G = list(map(int, input().split()))
    lead = G[0]
    stack = [(G[i], i) for i in range(M)]
    while stack:
        g, metal = stack.pop()
        if metal == 1:  # lead
            lead += g
        else:
            for R2 in formulas[metal]:
                if g > 0 and R2 != metal:
                    stack.append((g - 1, R2))
                    break
    print(f"Case #{_+1}: {lead % (1000000007)}")