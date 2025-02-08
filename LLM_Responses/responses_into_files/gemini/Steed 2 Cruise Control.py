def solve():
    D, N = map(int, input().split())
    horses = []
    for _ in range(N):
        horses.append(list(map(int, input().split())))

    max_time = 0
    for k, s in horses:
        max_time = max(max_time, (D - k) / s)

    return D / max_time

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")