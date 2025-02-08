def solve():
    S, D = input().split()
    D = int(D)
    N = len(S)
    MOD = 1000000007

    ans = 0
    for i in range(1 << (N - 1)):
        division = []
        current_num = ""
        for j in range(N):
            current_num += S[j]
            if j == N - 1 or (i >> j) & 1:
                division.append(int(current_num))
                current_num = ""

        divisible = True
        for k in range(len(division) - 1):
            if division[k] % D != 0 and division[k+1] % D != 0:
                divisible = False
                break
        
        if divisible:
            ans = (ans + 1) % MOD

    return ans

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")