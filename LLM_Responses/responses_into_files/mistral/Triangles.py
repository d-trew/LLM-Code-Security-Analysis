import sys
input = sys.stdin.readlines

def max_triangles(points):
    n = len(points)
    triangles = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_valid([points[i], points[j], points[k]]):
                    triangles.add((i,j,k))
    return len(triangles, triangles)

def is_valid(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    area = abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)
    return area > 0 and (abs(x1 - x2) + abs(y1 - y2) + abs(x2 - x3) + abs(y2 - y3) + abs(x3 - x1) + abs(y3 - y1)) < 2*(10**9)

T = int(input().strip())
for t in range(1, T+1):
    N = int(input().strip())
    points = [tuple(map(int, input().strip().split())) for _ in range(N)]
    triangles = max_triangles(points)
    print("Case #{}: {}".format(t, triangles[0]))
    if triangles[1]:
        for triangle in triangles[1]:
            print("\n  {} {} {}".format(*triangle))



This code reads the number of test cases from the standard input and iterates through each test case. For each test case, it reads the number of points and their coordinates, checks if a triangle is valid using the area formula and distance comparison, and stores the valid triangles in a set. Finally, it prints the maximum size of the set of triangles found and the vertices of the triangles if any.