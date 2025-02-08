def solve():
    C = int(input())
    tours = []
    for i in range(2 * C):
        E, L, D = map(int, input().split())
        tours.append((E, L, D))

    min_time = float('inf')

    import itertools

    for perm in itertools.permutations(range(2 * C)):
        current_time = 0
        current_camp = 1
        valid = True
        total_time = 0

        for tour_index in perm:
            E, L, D = tours[tour_index]
            start_camp = (tour_index // 2) + 1

            if current_camp != start_camp:
                valid = False
                break

            arrival_time = current_time + L + D
            
            if arrival_time > 23:
                days = (arrival_time - 23 + 23) // 24
                total_time += (days * 24) + arrival_time - (days * 24)
            else:
                total_time += arrival_time
            current_time = arrival_time
            current_camp = E

        if valid and current_camp == 1:
            min_time = min(min_time, total_time)

    return min_time


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")