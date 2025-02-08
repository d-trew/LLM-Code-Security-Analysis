def solve():
    F, P = map(int, input().split())
    pairs = []
    for _ in range(P):
        pairs.append(list(map(int, input().split())))

    adj = [[] for _ in range(F + 1)]
    for i, (u, v) in enumerate(pairs):
        adj[u].append((v, i))

    
    for i in range(1 << P):
        news = [0] * P
        given = [0] * (F + 1)
        received = [0] * (F + 1)
        
        for j in range(P):
            if (i >> j) & 1:
                news[j] = 1
            else:
                news[j] = -1

        valid = True
        for j in range(P):
            u, v = pairs[j]
            given[u] += news[j]
            received[v] += news[j]

        for k in range(1, F + 1):
            if given[k] != received[k]:
                valid = False
                break
        
        if valid:
            return " ".join(map(str, news))

    return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")