T = int(input())
for _ in range(T):
    K, Q = map(int, input().split())
    P = input()
    for _ in range(Q):
        S, E = map(int, input().split())
        N = min(E - S + 1, S) if (S % 2 == 0 and E % 2 != 0) or (S % 2 != 0 and E % 2 == 0) else abs(S - E)
    print(f"Case #{_+1}: {N}")