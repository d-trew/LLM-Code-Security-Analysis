from itertools import permutations
for _ in range(int(input())):
    n, m = map(int, input().split())
    d = [int(x) for x in input().split()]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u-1, v-1))
    min_latencies = 0
    for p in permutations(range(n-1)):
        latencies = [0] * m
        for i, edge in enumerate(edges):
            if d[edge[0]] < d[edge[1]]:
                latencies[i] = -d[edge[0]]
            elif d[edge[0]] > d[edge[1]]:
                latencies[i] = -d[edge[1]]
            else:
                latencies[i] = 0
        valid = True
        for i, latency in enumerate(latencies):
            if latency < 0 and p[i] != edge[0]:
                valid = False
                break
        if valid:
            min_latencies += 1
    print(f"Case #{_+1}: {' '.join(map(str, latencies))}")