T = int(input())
for _ in range(T):
    M = int(input())
    formulas = {}
    for i in range(M-1):
        a, b = map(int, input().split())
        if (a, b) not in formulas:
            formulas[(a, b)] = 0
        if (b, a) not in formulas:
            formulas[(b, a)] = 0
    treasury = list(map(int, input().split()))
    lead = 0
    while sum(treasury[1:]) > 0:
        for i in range(M-1):
            a, b = [k for k, v in enumerate(treasury) if v > 0][i], [k for k, v in enumerate(treasury) if v > 0][i+1]
            if (a, b) in formulas or (b, a) in formulas:
                if treasury[a] >= 2 and treasury[b] >= 2:
                    lead += 2
                    treasury[a] -= 2
                    treasury[b] -= 2
    print(f"Case # {_+1}: {lead}")