Here is the Python code for this problem based on the description:


import sys
from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

def dot_product(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))

def cross_product(v1, v2):
    x = v1[1]*v2[2] - v1[2]*v2[1]
    y = v1[2]*v2[0] - v1[0]*v2[2]
    z = v1[0]*v2[1] - v1[1]*v2[0]
    return (x, y, z)

def angle(p1, p2):
    dz = dot_product(p1, p2)
    dx = sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    return abs(dz/dx if dx else 0)

def solve():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    
    prev_point = points[0]
    total = 0.0
    for point in points[1:]:
        total += distance(prev_point, point)
        prev_point = point
        
    if angle(points[-1], points[0]) < sqrt(2)/2:
        return "NO"
    
    for i in range(-1, len(points)-1):
        p1, p2, p3 = points[i-1], points[i], points[(i+1)%len(points)]
        
        v1 = (p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2])
        v2 = (p3[0]-p2[0], p3[1]-p2[1], p3[2]-p2[2])
        
        dv = cross_product(v1, v2)
        if dot_product(dv, points[(i+2)%len(points)]) < 0:
            return "NO"
    
    if total > 4*sqrt(3):
        return "YES"
    else:
        return "NO"
        
t = int(input())
for i in range(1, t+1):
    print("Case #%d:" %i, solve())