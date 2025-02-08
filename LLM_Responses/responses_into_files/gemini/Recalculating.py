def solve():
    N, D = map(int, input().split())
    centers = []
    for _ in range(N):
        centers.append(list(map(int, input().split())))

    def info(x, y):
        info_set = set()
        for cx, cy in centers:
            if abs(cx - x) + abs(cy - y) <= D:
                info_set.add((cx - x, cy - y))
        return frozenset(info_set)

    total_area = 0
    distinguishable_area = 0

    min_x = min(c[0] for c in centers) - D
    max_x = max(c[0] for c in centers) + D
    min_y = min(c[1] for c in centers) - D
    max_y = max(c[1] for c in centers) + D

    
    step = 0.001

    for x in [min_x + i * step for i in range(int((max_x - min_x)/step))]:
        for y in [min_y + i * step for i in range(int((max_y - min_y)/step))]:
            
            if any(abs(c[0] - x) + abs(c[1] - y) <= D for c in centers):
                total_area += step**2
                
                is_distinguishable = True
                for x2 in [min_x + i * step for i in range(int((max_x - min_x)/step))]:
                    for y2 in [min_y + i * step for i in range(int((max_y - min_y)/step))]:
                        if any(abs(c[0] - x2) + abs(c[1] - y2) <= D for c in centers):
                            if info(x, y) == info(x2, y2) and (x,y) != (x2,y2):
                                is_distinguishable = False
                                break
                    if not is_distinguishable:
                        break
                if is_distinguishable:
                    distinguishable_area += step**2


    num = int(round(distinguishable_area))
    den = int(round(total_area))

    
    common_divisor = gcd(num, den)
    return f"{num // common_divisor} {den // common_divisor}"

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")