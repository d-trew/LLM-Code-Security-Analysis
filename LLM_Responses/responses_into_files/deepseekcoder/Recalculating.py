from collections import Counter

def calculate_probability(D):
    total_area = D * D * 4
    red_area = (2 * D + 1) ** 2 - (D - 1) ** 2
    blue_area = total_area - red_area
    distinguishable_area = red_area
    non_distinguishable_area = blue_area

    if D == 1:
        return 0, 1

    probability = float(red_area) / float(total_area)
    return int(probability * (10 ** 9)) % (10 ** 9), total_area

T = int(input())
for t in range(T):
    N, D = map(int, input().split())
    repair_centers = []
    for _ in range(N):
        x, y = map(int, input().split())
        repair_centers.append((x, y))
    
    red_points = set()
    for i in range(-D, D+1):
        for j in range(-D, D+1):
            if abs(i) + abs(j) <= D:
                for center in repair_centers:
                    if abs(i - center[0]) + abs(j - center[1]) <= D:
                        red_points.add((i, j))
    
    distinguishable_area = len(red_points)
    non_distinguishable_area = (2 * D + 1) ** 2 - distinguishable_area
    
    probability, total_area = calculate_probability(D)
    print("Case #{}: {}".format(t+1, str(probability) + " " + str(total_area)))