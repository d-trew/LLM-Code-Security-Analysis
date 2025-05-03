import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def is_collinear(p1, p2, p3):
    return (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p1[1] * (p2[0] - p3[0])) == 0 and \
           (p1[1] * (p2[2] - p3[2]) + p2[1] * (p3[2] - p1[2]) + p1[2] * (p2[0] - p3[0])) == 0 and \
           (p1[2] * (p2[0] - p3[0]) + p2[2] * (p3[1] - p1[0]) + p1[0] * (p2[2] - p3[1])) == 0

def is_omnicircumnavigation(points):
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        if distance(p1, p2) < 2: # same point or antipodes
            return False
        for j in range((i + 2) % len(points), (i - 1):
            p3 = points[j]
            if is_collinear(p1, p2, p3):
                return False
    return True

def main():
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        points = []
        for j in range(N):
            x, y, z = map(int, input().split())
            r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
            points.append((x / r, y / r, z / r))
        print("Case #%d: %s" % (i, "YES" if is_omnicircumnavigation(points) else "NO"))

main()