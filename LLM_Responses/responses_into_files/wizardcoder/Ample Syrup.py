import math

def max_exposed_area(N, K):
    pancakes = []
    for _ in range(N):
        R, H = map(int, input().split())
        pancakes.append([R, H])
    
    pancakes.sort(key=lambda x: x[0], reverse=True)
    pancakes_used = []
    for i in range(K):
        pancakes_used.append(pancakes.pop())
    
    total_exposed_area = 0
    for pancake in pancakes_used:
        R, H = pancake[0], pancake[1]
        if len(pancakes_used) == 1:
            total_exposed_area += math.pi * R ** 2 + 2 * math.pi * R * H
        else:
            total_exposed_area += 2 * math.pi * R * pancakes_used[-1][0] + 2 * math.pi * R * H
    
    return round(total_exposed_area, 6)

T = int(input())
for i in range(1, T+1):
    N, K = map(int, input().split())
    print("Case #{}: {}".format(i, max_exposed_area(N, K))