from collections import Counter
def count_ways(N, C, A, B):
    ways = 0
    for i in range(N+1):
        if i < 2:
            continue
        colors = [0] * (C + 1)
        geese = []
        for j in range(N):
            if j % N == i - 1:
                geese.append(Counter({P_j: 1 for P_j in P}))
        for color, count in Counter().items():
            diff = sum(a <= k <= b for k, a, b in zip(geese, A[color-1], B[color-1])) - count
            if diff < 0:
                return ways
            ways += diff
    return ways

T = int(input())
for t in range(T):
    N, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(C)]
    P = list(map(int, input().split()))
    print(f"Case #{t+1}: {count_ways(N, C, [a[0] for a in A], [a[1] for a in A])}")