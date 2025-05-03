def draw_circle_filled(R):
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if x**2 + y**2 <= R**2:
                set_pixel_to_black(x, y)

def draw_circle_filled_wrong(R):
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if (x-R)**2 + (y-R)**2 <= R**2:
                set_pixel_to_black(x, y)

def count_different_colors(R):
    num_different_colors = 0
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if get_pixel_color(x, y) != get_pixel_color(x-R, y-R):
                num_different_colors += 1
    return num_different_colors