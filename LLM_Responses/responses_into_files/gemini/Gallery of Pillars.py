def solve():
    N, R = map(int, input().split())
    R = R / 1000000.0

    visible_count = 0
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue

            blocked = False
            x = j + 0.5
            y = i + 0.5

            for k in range(N):
                for l in range(N):
                    if k == i and l == j:
                        continue
                    
                    x2 = l + 0.5
                    y2 = k + 0.5
                    
                    if (y2 - y) * x - (x2 - x) * y > 0:
                        
                        dist_to_pillar = abs((y2-y)*x - (x2-x)*y)/((y2-y)**2 + (x2-x)**2)**0.5
                    
                        if dist_to_pillar < R:
                            blocked = True
                            break
                if blocked:
                    break
            if not blocked:
                visible_count += 1

    return visible_count

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")