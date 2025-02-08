def solve():
    n = int(input())
    
    max_polygons = 1
    
    def count_polygons(current_sides, num_polygons, current_polygon_sides):
        nonlocal max_polygons
        max_polygons = max(max_polygons, num_polygons)

        if current_sides == n:
            return

        for i in range(current_polygon_sides -1, 2, -1):
            if current_polygon_sides % i == 0 and current_sides + i <=n:
                count_polygons(current_sides + i, num_polygons + 1, i)


    for i in range(3, n + 1):
        count_polygons(i, 1, i)

    return max_polygons


t = int(input())
for i in range(1, t + 1):
    result = solve()
    print(f"Case #{i}: {result}")