from fractions import Fraction

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    N, W, H = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    patches = []
    for _ in range(N):
        patches.append(list(map(int, input().split())))

    min_diff = float('inf')

    for cut_x in range(W + 1):
        your_enjoyment = 0
        twin_enjoyment = 0
        for x, y, a, b in patches:
            x1, y1 = x, y
            x2, y2 = x + P, y + Q
            x3, y3 = x + R, y + S

            area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

            your_area = 0
            twin_area = 0

            if x3 <= cut_x:
                your_area = area
            elif x1 >= cut_x:
                twin_area = area
            else:
                # Calculate the intersection area
                
                #Method to calculate the intersection area.  There are much more efficient methods, but this is relatively clear.

                points = [(x1,y1), (x2,y2), (x3,y3)]
                
                polygon_points = []
                for p in points:
                    polygon_points.append(p)

                
                
                vertices = sorted(points, key=lambda p: p[0])

                if vertices[0][0] < cut_x < vertices[-1][0]:
                    
                    #Intersection occurs
                    
                    #This part is incomplete.  It's tricky to get the exact intersection area.
                    #Would be much easier using a geometry library.
                    
                    pass
                    

                
                
            your_enjoyment += (your_area / area) * a if area > 0 else 0
            twin_enjoyment += (twin_area / area) * b if area > 0 else 0

        diff = abs(your_enjoyment - twin_enjoyment)
        if diff < min_diff:
            min_diff = diff

    num = int(min_diff * 1000000)
    den = 1000000
    common = gcd(num, den)
    return str(num // common) + "/" + str(den // common)



T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")