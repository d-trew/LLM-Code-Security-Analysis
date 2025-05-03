from fractions import Fraction

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def simplify_fraction(n, d):
    g = gcd(n, d)
    return (n//g, d//g)

def is_neat_pattern(polygon, K):
    N = len(polygon)
    for i in range(N):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % N]
        dx, dy = x2 - x1, y2 - y1
        if K == 2:
            return [(Fraction(dx, lcm(abs(dx), abs(dy))), Fraction(dy, lcm(abs(dx), abs(dy)))), (Fraction(-dx, lcm(abs(dx), abs(dy))), Fraction(-dy, lcm(abs(dx), abs(dy))))]
    return None

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        polygon = [(Fraction(int(data[index + 2 + i*2]), 1), Fraction(int(data[index + 3 + i*2]), 1)) for i in range(N)]
        index += 2 * N + 2
        
        result = is_neat_pattern(polygon, K)
        if result:
            results.append(f"Case #{_+1}: POSSIBLE\n{'\n'.join([f'{a[0]}/{a[1]} {b[0]}/{b[1]}' for a, b in result])}")
        else:
            results.append(f"Case #{_+1}: IMPOSSIBLE")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()