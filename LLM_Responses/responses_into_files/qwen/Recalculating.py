from fractions import Fraction

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def solve(N, D, repair_centers):
    total_area = 0
    distinguishable_area = 0
    
    for i in range(N):
        x1, y1 = repair_centers[i]
        for j in range(i + 1, N):
            x2, y2 = repair_centers[j]
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            if dx + dy <= D:
                area = (D - dx) * (D - dy)
                total_area += area
                distinguishable_area += area
    
    for i in range(N):
        x1, y1 = repair_centers[i]
        for dx in range(-D, D + 1):
            for dy in range(-D, D + 1):
                if abs(dx) + abs(dy) > D:
                    continue
                found = False
                for j in range(N):
                    if i != j and abs(x1 - repair_centers[j][0] - dx) + abs(y1 - repair_centers[j][1] - dy) <= D:
                        found = True
                        break
                if not found:
                    distinguishable_area += 1
    
    return Fraction(distinguishable_area, total_area)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        D = int(data[index + 1])
        repair_centers = []
        index += 2
        
        for _ in range(N):
            x = int(data[index])
            y = int(data[index + 1])
            repair_centers.append((x, y))
            index += 2
        
        result = solve(N, D, repair_centers)
        results.append(result)
    
    for i, result in enumerate(results, start=1):
        print(f"Case #{i}: {result.numerator} {result.denominator}")

if __name__ == "__main__":
    main()