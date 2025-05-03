import random
from math import pi, sin, cos, sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def orientation(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def is_parallel(x1, y1, x2, y2, x3, y3, x4, y4):
    return orientation(x1, y1, x2, y2, x3, y3) == 0 and orientation(x1, y1, x2, y2, x4, y4) != 0

def is_perpendicular(x1, y1, x2, y2, x3, y3, x4, y4):
    return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1) and (x2 - x1) * (y4 - y1) != (y2 - y1) * (x4 - x1)

def intersects(x1, y1, x2, y2, x3, y3):
    return is_parallel(x1, y1, x2, y2, x3, y3) or is_perpendicular(x1, y1, x2, y2, x3, y3)

def angle(theta):
    return (theta - pi / 2) % (2 * pi)

def get_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return atan2(dy, dx)

def is_on_segment(x1, y1, x2, y2, x3, y3):
    dx = x2 - x1
    dy = y2 - y1
    return 0 <= (x3 * dx + y3 * dy) / sqrt(dx ** 2 + dy ** 2) <= distance(x1, y1, x2, y2)

def is_clockwise(theta):
    return theta % (2 * pi) < pi

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        lasers = []
        for j in range(N):
            x1, y1, x2, y2, x3, y3 = map(int, input().split())
            lasers.append((x1, y1, x2, y2))

        clockwise_lasers = [0] * N
        counterclockwise_lasers = [0] * N
        for j in range(N):
            x1, y1, x2, y2 = lasers[j][:2]
            theta = get_angle(x1, y1, x2, y2)
            if is_on_segment(-500, 0, 0, 100, y1):
                clockwise_lasers[j] = is_clockwise(theta)
            else:
                counterclockwise_lasers[j] = not is_clockwise(theta)
        total = sum(clockwise_lasers + counterclockwise_lasers)
        if total == 0:
            print("Case #{}: {}".format(i + 1, 1.0))
        else:
            probability = random.random() * (2 * pi - N / total) ** 2
            print("Case #{}: {}".format(i + 1, probability))

if __name__ == "__main__":
    main()