import math

def draw_circle_filled(R):
    pixels = set()
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            if x**2 + y**2 <= R**2:
                pixels.add((x, y))
    return pixels

def draw_circle_filled_wrong(R):
    pixels = set()
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            if abs(x) + abs(y) <= R:
                pixels.add((x,y))
    return pixels

T = int(input())
for x in range(1, T + 1):
    R = int(input())
    correct_pixels = draw_circle_filled(R)
    wrong_pixels = draw_circle_filled_wrong(R)
    diff = len(correct_pixels.symmetric_difference(wrong_pixels))
    print(f"Case #{x}: {diff}")