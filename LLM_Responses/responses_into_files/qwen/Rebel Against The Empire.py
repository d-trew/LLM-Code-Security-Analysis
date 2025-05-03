import math

def calculate_max_jump(N, S, asteroids):
    def distance(a, b):
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

    max_jump = float('inf')
    for i in range(N):
        for j in range(i + 1, N):
            d = distance(asteroids[i], asteroids[j])
            if d < max_jump:
                max_jump = d
    return max_jump

def solve():
    T = int(input())
    results = []
    for t in range(T):
        N, S = map(int, input().split())
        asteroids = [tuple(map(float, input().split())) for _ in range(N)]
        result = calculate_max_jump(N, S, asteroids)
        results.append(f"Case #{t+1}: {result:.4f}")
    for result in results:
        print(result)

solve()