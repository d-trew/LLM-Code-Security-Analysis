from itertools import chain, product

def draw_circle_filled(R):
    matrix = [[0] * (2*R+1) for _ in range(2*R+1)]
    for x, y in product(range(-R, R+1), repeat=2):
        if abs(x) + abs(y) <= R:
            matrix[y][x] = 1
    return matrix

def draw_circle_filled_wrong(R):
    matrix = [[0] * (2*R+1) for _ in range(2*R+1)]
    for y in range(-R, R+1):
        row = matrix[y]
        for x in range(-R, R+1):
            if abs(x - R) <= abs(y) <= R:
                row[x] = 1
    return matrix

def count_diff_pixels(matrix1, matrix2):
    return sum(map(lambda x, y: (x != y).sum(), zip(*chain(matrix1, matrix2))))

def main():
    T = int(input())
    for _ in range(T):
        R = int(input())
        matrix1 = draw_circle_filled(R)
        matrix2 = draw_circle_filled_wrong(R)
        print(f"Case #{_+1}: {count_diff_pixels(matrix1, matrix2)}")

main()