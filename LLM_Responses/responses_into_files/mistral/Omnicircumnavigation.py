from math import sqrt, pi, acos, sin, cos
import sys
input = sys.stdin.readline

def is_great_circle(points):
    n = len(points)
    if n < 4:
        return False

    # Precompute cross product between each pair of vectors
    cross_products = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            xi, yi, zi = points[i]
            xj, yj, zj = points[j]
            cross_products[i][j] = (yi * zj - zi * yj,
                                   zi * xj - xi * zj,
                                   xi * yj - yi * xj)
    # Check if every point is on a great circle passing through two other points
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p_ij = cross_products[i][j]
                p_jk = cross_products[j][k]
                p_ik = cross_products[i][k]
                if all([p_ij[0] * p_jk[0] == p_ik[0],
                        p_ij[1] * p_jk[1] == p_ik[1],
                        p_ij[2] * p_jk[2] == p_ik[2]]):
                    return False
    # Check if every point is on a great circle passing through the first and last points
    for i in range(n):
        for j in range(i + 1, n):
            cross_product = cross_products[0][j]
            if all([cross_product[0] * points[i][2] == points[j][2],
                    cross_product[1] * points[i][0] == points[j][0],
                    cross_product[2] * points[i][1] == points[j][1]]):
                return False
    # Check if the path forms a closed loop that touches every hemisphere
    path = [points[0]]
    for i in range(1, n):
        next_point = path[-1]
        while True:
            dots_product = next_point[0] * points[i][0] + next_point[1] * points[i][1] + next_point[2] * points[i][2]
            if dots_product <= 0:
                next_point[0], next_point[1], next_point[2] = -next_point[0], -next_point[1], -next_point[2]
            if (next_point == points[i]) or (dots_product > 0):
                path.append(points[i])
                break
    if len(path) != n:
        return False
    for i in range(n):
        hemisphere = 2 * (1 - int((pi / 2) - acos(min([cos(points[i][0]), cos(path[(i + 1) % n][0]])) > 0)) / pi)
        if hemisphere != 3:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    points = []
    for _ in range(n):
        x, y, z = map(float, input().split())
        points.append((x / sqrt(x * x + y * y + z * z), y / sqrt(x * x + y * y + z * z), z / sqrt(x * x + y * y + z * z)))
    print("Case #{}: {}".format(_ + 1, "YES" if is_great_circle(points) else "NO"))


This Python code reads test cases from standard input and checks whether a given sequence of points forms an omnicircumnavigation. The function `is_great_circle` takes a list of points as input, precomputes the cross product between each pair of vectors, and then checks if every point is on a great circle passing through two other points. It also checks if the path forms a closed loop that touches every hemisphere by iterating through the points and checking if they belong to the same or opposite hemisphere as the first point. The code prints the result for each test case in the format "Case #x: YES" or "Case #x: NO", where x is the case number.