import fractions
from collections import defaultdict
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def solve(triangles, w, h):
    n = len(triangles)
    area = defaultdict(int)
    for x1, y1, a, _ in triangles:
        area[(x1, y1)] += abs(a)

    # Calculate the area of the cake
    total_area = lcm(w, h)
    min_diff = float('inf')

    for x in range(total_area + 1):
        left_area = sum([area[(x1, y)] for x1, _, _, _ in triangles if x <= x1 < (x + w)])
        right_area = total_area - left_area

        diff = abs(left_area - right_area)
        min_diff = min(min_diff, diff)

    # The result may have a large numerator and denominator. Convert it to lowest terms.
    g = math.gcd(min_diff, total_area)
    return str(fractions.Fraction(min_diff // g, total_area // g))

T = int(input())
for t in range(1, T + 1):
    w, h, n = map(int, input().split())
    triangles = []
    for _ in range(n):
        x1, y1, a, b = map(int, input().split())
        triangles.append((x1, y1, a, b))
    print(f"Case # {t}: {solve(triangles, w, h)}")