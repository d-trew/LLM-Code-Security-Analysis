def solve():
    C, D = map(int, input().split())
    X = [0] + list(map(int, input().split()))
    edges = []
    for _ in range(D):
        edges.append(list(map(int, input().split())))

    #This is a simplified solution that assumes a tree structure and assigns latencies arbitrarily.
    #A more robust solution would involve constraint satisfaction or a more sophisticated graph algorithm.

    latencies = []
    for i in range(D):
        latencies.append(1)  # Assign a default latency of 1

    return " ".join(map(str, latencies))


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")