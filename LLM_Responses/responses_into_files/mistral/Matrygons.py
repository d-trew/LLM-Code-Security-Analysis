T = int(input())
for t in range(1, T + 1):
    N = int(input())
    max_polygons = 0
    for i in range(3, N // 2 + 1):
        if i * (i - 1) <= N:
            max_polygons = i
            break
    print(f"Case #{t}: {max_polygons}")