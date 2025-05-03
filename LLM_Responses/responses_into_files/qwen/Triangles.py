T = int(input())
for t in range(1, T + 1):
    N = int(input())
    P = []
    for _ in range(N):
        x, y = map(int, input().split())
        P.append((x, y))
    max_triangles = 0
    triangles = set()
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                p1, q1 = P[i]
                p2, q2 = P[j]
                p3, q3 = P[k]
                if (q2 - q1) * (p3 - p1) == (q3 - q1) * (p2 - p1):
                    continue
                triangles.add((i + 1, j + 1, k + 1))
    print(f"Case #{t}: {len(triangles)}")
    for triangle in sorted(list(triangles)):
        print(*triangle, sep=' ')