import math

def solve():
    N, K = map(int, input().split())
    pancakes = []
    for _ in range(N):
        r, h = map(int, input().split())
        pancakes.append((r, h))

    max_area = 0
    
    for i in range(1 << N):
        chosen_pancakes = []
        count = 0
        for j in range(N):
            if (i >> j) & 1:
                chosen_pancakes.append(pancakes[j])
                count += 1
        
        if count != K:
            continue

        chosen_pancakes.sort(reverse=True, key=lambda x: x[0])
        
        total_area = 0
        
        if len(chosen_pancakes)>0:
            total_area += math.pi * chosen_pancakes[0][0] ** 2 + 2 * math.pi * chosen_pancakes[0][0] * chosen_pancakes[0][1]
            
            for k in range(1,len(chosen_pancakes)):
                total_area += 2 * math.pi * chosen_pancakes[k][0] * chosen_pancakes[k][1] + math.pi * chosen_pancakes[k][0]**2 - math.pi * chosen_pancakes[k-1][0]**2

        max_area = max(max_area, total_area)

    return max_area

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")