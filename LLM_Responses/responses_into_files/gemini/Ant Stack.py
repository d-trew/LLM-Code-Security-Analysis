def solve():
    N = int(input())
    weights = list(map(int, input().split()))

    max_ants = 0
    for i in range(1 << N):
        stack = []
        current_weight = 0
        count = 0
        for j in range(N):
            if (i >> j) & 1:
                if not stack:
                    stack.append(weights[j])
                    current_weight += weights[j]
                    count += 1
                else:
                    if stack[-1] * 6 >= current_weight + weights[j]:
                        stack.append(weights[j])
                        current_weight += weights[j]
                        count += 1
                    else:
                        break

        max_ants = max(max_ants, count)

    return max_ants

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")