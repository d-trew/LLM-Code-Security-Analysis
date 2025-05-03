def reversort_engineering(N, C):
    if N * (N - 1) // 2 < C or C % 2 != N % 2:
        return "IMPOSSIBLE"
    
    if N == 1:
        return "1"
    
    result = list(range(1, N + 1))
    cost = 0
    
    for i in range(N - 1):
        j = C - (N - i - 1)
        result[:j] = reversed(result[:j])
        cost += j
        if cost == C:
            break
    
    return " ".join(map(str, result))

T = int(input())
results = []
for t in range(1, T + 1):
    N, C = map(int, input().split())
    results.append(f"Case #{t}: {reversort_engineering(N, C)}")

for result in results:
    print(result)