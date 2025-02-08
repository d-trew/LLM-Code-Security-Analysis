def solve():
    R, C, F, S = map(int, input().split())
    current = [input() for _ in range(R)]
    target = [input() for _ in range(R)]

    diff_count = 0
    for r in range(R):
        for c in range(C):
            if current[r][c] != target[r][c]:
                diff_count += 1

    if diff_count == 0:
        return 0

    if S >= 2 * F:
        return diff_count * F
    else:
        return (diff_count // 2) * S + (diff_count % 2) * F

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")