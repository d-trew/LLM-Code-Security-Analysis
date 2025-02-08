def solve():
    K, C, S = map(int, input().split())
    
    if C == 1:
        if S >= 1:
            return " ".join(map(str, range(1, min(S + 1, K + 1))))
        else:
            return "IMPOSSIBLE"

    total_tiles = K**C
    
    if S >= K:
        positions = []
        for i in range(1,K+1):
            positions.append(i)
        return " ".join(map(str, positions))

    
    if K == 1:
      return "1"
    
    if S < K:
        return "IMPOSSIBLE"

    

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")