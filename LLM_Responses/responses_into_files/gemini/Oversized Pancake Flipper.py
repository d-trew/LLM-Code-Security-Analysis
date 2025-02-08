def solve():
    S, K = input().split()
    K = int(K)
    S = list(S)
    n = len(S)
    
    flips = 0
    for i in range(n - K + 1):
        if S[i] == '-':
            flips += 1
            for j in range(i, i + K):
                S[j] = '+' if S[j] == '-' else '-'

    for i in range(n):
        if S[i] == '-':
            return "IMPOSSIBLE"
    
    return flips

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")