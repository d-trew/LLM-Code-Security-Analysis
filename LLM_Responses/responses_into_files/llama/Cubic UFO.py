import math

def calculate_shadow_area(cube_points):
    shadow_xmin = min(x1 for x1, _, _ in cube_points)
    shadow_xmax = max(x2 for _, x2, _ in cube_points)
    shadow_ymin = -3
    shadow_ymax = -3
    for x1, _, z1 in cube_points:
        if abs(z1) > 0.5:
            shadow_ymin = min(shadow_ymin, -3 - 0.5 + abs(z1))
            shadow_ymax = max(shadow_ymax, -3 + 0.5 - abs(z1))

    shadow_width = shadow_xmax - shadow_xmin
    shadow_height = shadow_ymax - shadow_ymin
    return shadow_width * shadow_height

def find_rotation(cube_points):
    x1, y1, z1 = cube_points[0]
    x2, y2, z2 = cube_points[1]
    if abs(y1) + abs(z1) > 0.5 and abs(y2) + abs(z2) > 0.5:
        return [x1, -y1, z1], [x2, -y2, z2], [x1, y1, z1]

    x1, y1, z1 = cube_points[0]
    x3, y3, z3 = cube_points[2]
    if abs(y1) + abs(z1) > 0.5 and abs(y3) + abs(z3) > 0.5:
        return [x1, -y1, z1], [x2, y2, z2], [x3, y3, z3]

    x1, y1, z1 = cube_points[0]
    x2, y2, z2 = cube_points[1]
    if abs(y1) + abs(z1) > 0.5 and abs(y2) + abs(z2) > 0.5:
        return [x1, -y1, z1], [x3, y3, z3], [x2, -y2, z2]

    for x1, y1, z1 in cube_points:
        if abs(y1) + abs(z1) > 0.5:
            return [x1, -y1, z1], [x2, y2, z2], [x3, y3, z3]

T = int(input())
for t in range(1, T+1):
    A = float(input())
    cube_points = [(0.5, 0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
                   (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5)]
    shadow_area = calculate_shadow_area(cube_points)
    if math.isclose(shadow_area, A):
        rotation_points = find_rotation(cube_points)
        print(f"Case #{t}:")
        for point in rotation_points:
            print(" ".join(map(str, point)))