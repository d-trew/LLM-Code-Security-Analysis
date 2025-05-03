from fractions import Fraction

def min_time_to_deliver(T, test_cases):
    results = []
    
    for i in range(1, T + 1):
        N, Ei, Si, D = test_cases[i-1]
        
        # Create adjacency list and horse endurance dictionary
        adj_list = [[] for _ in range(N)]
        horse_endurance = [0] * N
        
        for j in range(Ei):
            u, v, d = D[j]
            if u != -1:
                adj_list[u].append((v, d))
                adj_list[v].append((u, d))
        
        for j in range(Si):
            u, e = D[Ei + j]
            horse_endurance[u] = e
        
        # Calculate minimum time to deliver from city 1 to city N
        start_time = Fraction(0)
        current_city = 0
        current_horse = 0
        used_distance = 0
        
        while current_city != N - 1:
            next_city = None
            min_time = float('inf')
            
            for neighbor, distance in adj_list[current_city]:
                if neighbor == N - 1:
                    time_to_neighbor = Fraction(distance, horse_endurance[neighbor])
                    if used_distance + distance <= horse_endurance[neighbor]:
                        if time_to_neighbor < min_time:
                            min_time = time_to_neighbor
                            next_city = neighbor
            
            if next_city is None:
                break
            
            start_time += min_time
            current_city = next_city
            used_distance = 0
        
        results.append(start_time)
    
    return results

# Example usage:
T = 3
test_cases = [
    (5, 4, 2, [(1, 2, 10), (2, 3, 10), (3, 4, 10), (4, 5, 10), (-1, -1, 1000), (1, 1000), (2, 1000)]),
    (6, 5, 2, [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (-1, -1, 1000), (1, 1000), (2, 1000)]),
    (7, 6, 2, [(1, 2, 100), (2, 3, 100), (3, 4, 100), (4, 5, 100), (5, 6, 100), (-1, -1, 1000), (1, 1000), (2, 1000)])
]

results = min_time_to_deliver(T, test_cases)
for i, result in enumerate(results):
    print(f"Case #{i+1}: {result}")