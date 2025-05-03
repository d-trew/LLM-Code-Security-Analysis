T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    count = 0
    for L in range(1, N+1):
        for R in range(L, N+1):
            if all(min(C[L-1:R]) <= max(C[L-1:R]) and min(D[L-1:R]) <= max(D[L-1:R]) for _ in range(R-L+1)):
                count += 1
    print(f"Case # {_ + 1}: {count}")