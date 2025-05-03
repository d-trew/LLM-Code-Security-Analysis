T = int(input())
for _ in range(T):
    R, C, F, S = map(int, input().split())
    current = [list(map(str, input().strip())) for _ in range(R)]
    desired = [list(map(str, input().strip())) for _ in range(R)]
    flips = sum(c != d for r in current for c, d in zip(r, desired))
    swaps = 0
    for i in range(R):
        for j in range(C - 1):
            if current[i][j] != desired[i][j] or current[i][j + 1] != desired[i][j + 1]:
                swaps += 1
            elif current[i][j] == desired[i][j + 1]:
                flips += 1
                breaks
    print(f"Case #{_ + 1}: {F * flips + S * swaps}")