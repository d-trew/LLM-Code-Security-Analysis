T = int(input())
for _ in range(T):
    N = int(input())
    Vs = list(map(int, input().split()))
    MOD = 1000000007
    ans = 0
    for i in range(N):
        ans += sum(1 for j in range(i+1) if Vs[j] >= i+1)
    print(f"Case # {_+1}: {ans % MOD}")