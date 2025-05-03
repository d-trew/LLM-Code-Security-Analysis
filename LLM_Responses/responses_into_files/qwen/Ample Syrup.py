import math

def max_exposed_area(N, K, pancakes):
    pancakes.sort(key=lambda x: -x[0])
    exposed_area = 0
    
    for i in range(K):
        radius, height = pancakes[i]
        if i == 0:
            exposed_area += math.pi * radius ** 2 + 2 * math.pi * radius * height
        else:
            prev_radius, _ = pancakes[i-1]
            exposed_area += 2 * math.pi * min(radius, prev_radius) * (height - abs(prev_radius - radius))
    
    return exposed_area

def main():
    T = int(input())
    results = []
    
    for case in range(1, T + 1):
        N, K = map(int, input().split())
        pancakes = [tuple(map(int, input().split())) for _ in range(N)]
        result = max_exposed_area(N, K, pancakes)
        results.append(f"Case #{case}: {result:.6f}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()