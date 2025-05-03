from fractions import Fraction

def calculate_probability(N, rays):
    def is_touching_segment(x, y):
        for x0, y0, x1, y1 in rays:
            dx = x1 - x0
            dy = y1 - y0
            if dx == 0 and (y < y0 or y > y1):
                continue
            t = Fraction(y - y0, dy)
            if 0 <= t <= 1 and abs(x - (x0 + t * dx)) <= 1e-6:
                return True
        return False

    def find_open_interval(rays):
        for i in range(N):
            x0, y0, x1, y1 = rays[i]
            if is_touching_segment(x0, y0):
                continue
            t = Fraction(y0 - 1000, y1 - y0)
            if 0 <= t < 1:
                return True
        return False

    probability = Fraction(1)
    for _ in range(N):
        if not find_open_interval(rays):
            probability *= Fraction(3, 4)
        else:
            probability *= Fraction(1, 4)
    return probability

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    for _ in range(T):
        N = int(data[index])
        index += 1
        rays = []
        for _ in range(N):
            x0, y0, x1, y1 = map(int, data[index:index+4])
            rays.append((x0, y0, x1, y1))
            index += 4
        
        result = calculate_probability(N, rays)
        results.append(f"Case #{_ + 1}: {result}")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()