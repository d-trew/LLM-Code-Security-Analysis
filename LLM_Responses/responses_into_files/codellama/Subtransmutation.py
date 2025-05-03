T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    U = list(map(int, input().split()))
    stack = [(0, [])]
    result = None
    while stack:
        i, path = stack.pop()
        if sum(U[j] for j in range(N) if j >= i) == 0:
            result = i
            break
        for j in range(i-1, -1, -1):
            if U[j] > 0:
                new_i = max(0, j-A)
                new_path = path + [(j, B-j)]
                stack.append((new_i, new_path))
    print(f"Case #{_+1}: {result if result is not None else 'IMPOSSIBLE'}")