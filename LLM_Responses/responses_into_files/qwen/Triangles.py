from itertools import combinations

def max_triangles(points):
    def is_triangle(p1, p2, p3):
        return (p1[0] * (p2[1] - p3[1]) +
                p2[0] * (p3[1] - p1[1]) +
                p3[0] * (p1[1] - p2[1])) != 0

    max_triangles = []
    for triplet in combinations(points, 3):
        if is_triangle(*triplet):
            max_triangles.append(triplet)
    return len(max_triangles), max_triangles

def solve():
    T = int(input())
    results = []
    for i in range(1, T + 1):
        N = int(input())
        points = [tuple(map(int, input().split())) for _ in range(N)]
        count, triangles = max_triangles(points)
        results.append(f"Case #{i}: {count}")
        for triangle in triangles:
            p, q, r = sorted(triangle, key=lambda x: (x[0], x[1]))
            results.append(f"{p[0]} {p[1]} {q[0]} {q[1]} {r[0]} {r[1]}")
    return '\n'.join(results)

print(solve())