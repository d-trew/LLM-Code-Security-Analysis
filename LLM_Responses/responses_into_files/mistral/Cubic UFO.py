import math

def rotate_cube(angle):
    rotation_matrix = [[math.cos(angle), -math.sin(angle), 0],
                       [math.sin(angle), math.cos(angle), 0],
                       [0, 0, 1]]

    points = [(0, 0, 0), (0.5, 0.5, 0), (0.5, -0.5, 0), (-0.5, 0.5, 0), (-0.5, -0.5, 0)]
    rotated_points = []

    for point in points:
        x, y, z = point
        rotated_x, rotated_y, rotated_z = [sum(i * j) for i, j in zip(rotation_matrix, [x, y, z])]
        rotated_points.append((rotated_x, -3, rotated_z))

    return rotated_points

def find_area(points):
    x1, y1, _ = points[0]
    x2, y2, _ = points[1]
    x3, y3, _ = points[2]

    area = abs((x1 - x2) * (y2 - y3) + (x2 - x3) * (y3 - y1) + (x3 - x1) * (y1 - y2)) / 2
    return area

def solve():
    T = int(input())

    for t in range(1, T+1):
        A = float(input())
        cube_area = find_area([(0, 0, 0), (0.5, 0.5, 0), (0.5, -0.5, 0)])

        angle = math.atan2((math.sqrt(2) * A - cube_area) / 2, cube_area / 2)
        rotated_points = rotate_cube(angle)

        print("Case #{}:".format(t))
        for point in rotated_points:
            print(" {}   {}    {}".format(*point))

solve()


This code calculates the area of the cube's shadow without rotation, then finds an appropriate angle to rotate the cube so that the projected area matches the desired value A. The cube is rotated around the x=y=0 line. Finally, it outputs the new coordinates for three points after the rotation and the test case number.