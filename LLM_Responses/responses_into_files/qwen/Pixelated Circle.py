T = int(input())
for i in range(T):
    R = int(input())
    wrong_pixels = set()
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if (x**2 + y**2)**0.5 <= R:
                wrong_pixels.add((x, y))
    correct_pixels = set()
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if (x**2 + y**2)**0.5 <= R:
                correct_pixels.add((x, y))
    diff_pixels = list(correct_pixels - wrong_pixels) + list(wrong_pixels - correct_pixels)
    print(f"Case #{i+1}: {len(diff_pixels)}")