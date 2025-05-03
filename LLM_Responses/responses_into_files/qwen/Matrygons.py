def max_polygons(N):
    if N < 3:
        return 1
    sides = [i for i in range(3, N + 1) if N % i == 0]
    return len(sides)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print(f"Case #{t}: {max_polygons(N)}")