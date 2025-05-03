T = int(input())
for t in range(T):
    M, N = map(int, input().split())
    formulas = []
    for _ in range(N):
        a, b = map(int, input().split())
        formulas.append((a,b))
    treasury = list(map(int, input().split()))
    max_lead = 0
    for f in formulas:
        if f[0] == 1 and f[1] == 2:
            max_lead += 2*treasury[1]
        elif f[0] == 3 and f[1] == 5:
            max_lead += 2*treasury[5]
    print("Case #" + str(t+1) + ": " + str(max_lead))