def solve():
    N, C = map(int, input().split())
    constraints = []
    for _ in range(C):
        constraints.append(list(map(int, input().split())))
    colors = list(map(int, input().split()))

    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            subset = colors[i:j+1]
            valid = True
            for k in range(C):
                color_count = subset.count(k + 1)
                if not (color_count == 0 or constraints[k][0] <= color_count <= constraints[k][1]):
                    valid = False
                    break
            if valid:
                count += 1
    return count

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")