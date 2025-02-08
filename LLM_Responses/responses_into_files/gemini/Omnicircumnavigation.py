import itertools

def solve():
    N = int(input())
    points = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        norm = (x**2 + y**2 + z**2)**0.5
        points.append((x / norm, y / norm, z / norm))

    def cross_product(a, b):
        return (a[1] * b[2] - a[2] * b[1],
                a[2] * b[0] - a[0] * b[2],
                a[0] * b[1] - a[1] * b[0])

    def dot_product(a, b):
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

    def is_omnicircumnavigation():
        for i in range(N):
            for j in range(i + 1, N):
                p1 = points[i]
                p2 = points[j]
                
                normal = cross_product(p1,p2)
                
                if all(x==0 for x in normal):
                    continue

                
                all_intersect = True
                for k in range(N):
                  
                    p3 = points[k]
                    if dot_product(normal,p3) > 0 :
                        all_intersect = all_intersect and True
                    elif dot_product(normal,p3) <0:
                        all_intersect = all_intersect and True
                    else:
                        all_intersect = False
                
                if not all_intersect:
                    return False
        return True

    return "YES" if is_omnicircumnavigation() else "NO"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")