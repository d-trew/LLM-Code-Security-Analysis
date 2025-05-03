T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    pancakes = []
    for _ in range(N):
        R, H = map(int, input().split())
        pancakes.append((R, H))
    pancakes.sort(key=lambda x: x[0], reverse=True)
    max_area = 0
    for i in range(K):
        R, H = pancakes[i]
        area = (2 * 3.14159 * R) + (2 * 3.14159 * R * H)
        max_area += area
    print(f"Case # {_+1}: {max_area:.6f}")