def find_crepe_cart(test_cases):
    results = []
    for t, (P, Q, people) in enumerate(test_cases, start=1):
        direction_counts = {}
        for x, y, d in people:
            if d == 'N':
                for y2 in range(y + 1, Q + 1):
                    key = (x, y2)
                    if key not in direction_counts:
                        direction_counts[key] = 0
                    direction_counts[key] += 1
            elif d == 'S':
                for y2 in range(y - 1, -1, -1):
                    key = (x, y2)
                    if key not in direction_counts:
                        direction_counts[key] = 0
                    direction_counts[key] += 1
            elif d == 'E':
                for x2 in range(x + 1, Q + 1):
                    key = (x2, y)
                    if key not in direction_counts:
                        direction_counts[key] = 0
                    direction_counts[key] += 1
            elif d == 'W':
                for x2 in range(x - 1, -1, -1):
                    key = (x2, y)
                    if key not in direction_counts:
                        direction_counts[key] = 0
                    direction_counts[key] += 1
        
        best_intersection = None
        max_count = 0
        for (x, y), count in direction_counts.items():
            if count > max_count or (count == max_count and (best_intersection is None or x < best_intersection[0] or (x == best_intersection[0] and y < best_intersection[1]))):
                best_intersection = (x, y)
                max_count = count
        
        results.append(f"Case #{t}: {best_intersection[0]} {best_intersection[1]}")
    
    return results

# Example usage:
test_cases = [
    (1, 10, [(5, 5, 'N')]),
    (4, 10, [(2, 5, 'N'), (2, 5, 'N'), (2, 5, 'N'), (2, 5, 'N')]),
    (8, 10, [(0, 0, 'E'), (0, 1, 'E'), (0, 2, 'E'), (0, 3, 'E'), (0, 4, 'E'), (0, 5, 'E'), (0, 6, 'E'), (0, 7, 'E')]),
]

print(find_crepe_cart(test_cases))