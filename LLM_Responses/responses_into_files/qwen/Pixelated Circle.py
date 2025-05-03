def draw_circle_filled(R):
    pixels = [[0] * (2*R + 1) for _ in range(2*R + 1)]
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if x*x + y*y <= R*R:
                pixels[x + R][y + R] = 1
    return pixels

def draw_circle_filled_wrong(R):
    pixels = [[0] * (2*R + 1) for _ in range(2*R + 1)]
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if abs(x*x - y*y) <= R*R:
                pixels[x + R][y + R] = 1
    return pixels

def count_different_pixels(R):
    filled = draw_circle_filled(R)
    wrong = draw_circle_filled_wrong(R)
    different_count = sum(1 for i in range(2*R+1) for j in range(2*R+1) if filled[i][j] != wrong[i][j])
    return different_count

T = int(input())
for t in range(1, T + 1):
    R = int(input())
    result = count_different_pixels(R)
    print(f"Case #{t}: {result}")