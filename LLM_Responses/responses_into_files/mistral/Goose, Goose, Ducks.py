T = int(input())
for t in range(1, T+1):
    N, M, S = map(int, input().split())
    meetings = []
    for _ in range(M):
        x, y, c = map(int, input().split())
        meetings.append((x, y, c))
    statements = []
    for _ in range(S):
        a, b, u, v, d = map(int, input().split())
        statements.append(((a, b), (u, v), d))
    min_ ducks = float('inf')
    for i in range(2**N):
        hypothesis = [0]*N
        for j in range(N):
            if (i >> j) & 1:
                hypothesis[j] = 1
            else:
                hypothesis[j] = 0
        if all(hypothesis[k] == 0 or all((a, b) != (c, d) and ((u, v), D) in meetings for (a, c), (b, d), U, V, D in statements):
            duck_count = sum(hypothesis)
            min_ ducks = min(min_ ducks, duck_count)
    print(f"Case #{t}: {min_ ducks}")