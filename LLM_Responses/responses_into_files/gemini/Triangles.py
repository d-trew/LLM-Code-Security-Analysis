def solve():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    def area(p1, p2, p3):
        return 0.5 * abs((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1]))

    def is_valid_triangle(p1, p2, p3):
        return area(p1, p2, p3) > 0

    max_triangles = 0
    best_triangles = []

    for i in range(1 << N):
        triangle_indices = []
        for j in range(N):
            if (i >> j) & 1:
                triangle_indices.append(j)

        if len(triangle_indices) % 3 != 0:
            continue

        triangles = []
        valid = True
        
        for k in range(0, len(triangle_indices), 3):
            p1_index = triangle_indices[k]
            p2_index = triangle_indices[k+1]
            p3_index = triangle_indices[k+2]
            
            if not is_valid_triangle(points[p1_index], points[p2_index], points[p3_index]):
                valid = False
                break
            triangles.append((p1_index + 1, p2_index + 1, p3_index + 1))

        if valid and len(triangles) > max_triangles:
            max_triangles = len(triangles)
            best_triangles = triangles


    return max_triangles, best_triangles


T = int(input())
for i in range(1, T + 1):
    max_triangles, best_triangles = solve()
    print(f"Case #{i}: {max_triangles}")
    for triangle in best_triangles:
        print(*triangle)