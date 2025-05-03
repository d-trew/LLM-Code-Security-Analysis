T = int(input())
for _ in range(T):
    N = int(input())
    F = list(map(int, input().split()))
    P = list(map(int, input().split()))
    initiators = [i for i in range(N) if P[i] == 0]
    funs = []
    for initiator in initiators:
        visited = set()
        max_fun = 0
        stack = [(initiator, F[initiator])]
        while stack:
            module, fun = stack.pop(0)
            if module not in visited:
                visited.add(module)
                if P[module] != 0:
                    stack.append((P[module], F[P[module]]))
                max_fun = max(max_fun, fun)
        funs.append(max_fun)
    print(f"Case #{_+1}: {sum(sorted(funs, reverse=True))}")