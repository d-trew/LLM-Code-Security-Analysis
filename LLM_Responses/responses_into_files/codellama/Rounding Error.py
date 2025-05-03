T = int(input())
for _ in range(T):
    N, L = map(int, input().split())
    C = list(map(int, input().split()))
    total = sum(C)
    remaining = N - total
    max_sum = 0
    for i in range(101):
        if (i + 1) * remaining <= 100:
            max_sum = max(max_sum, i * L + sum(min(i+1, c) for c in C))
    print(f"Case #{_+1}: {max_sum}")