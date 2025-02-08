def solve():
    N = int(input())
    F = list(map(int, input().split()))
    P = list(map(int, input().split()))

    initiators = []
    in_degree = [0] * N
    for i in range(N):
        if P[i] != 0:
            in_degree[P[i]-1] += 1
    for i in range(N):
        if in_degree[i] == 0:
            initiators.append(i)

    max_fun = 0
    import itertools
    for order in itertools.permutations(initiators):
        total_fun = 0
        triggered = [False] * N
        for initiator in order:
            current_fun = 0
            current_module = initiator
            while current_module != -1 and not triggered[current_module]:
                triggered[current_module] = True
                current_fun = max(current_fun, F[current_module])
                if P[current_module] == 0:
                    current_module = -1
                else:
                    current_module = P[current_module] -1
            total_fun += current_fun
        max_fun = max(max_fun, total_fun)
    return max_fun

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")