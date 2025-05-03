def calculate_interest_level(T, test_cases):
    results = []
    
    for i in range(T):
        R, C = test_cases[i]['R'], test_cases[i]['C']
        grid = test_cases[i]['grid']
        
        def get_neighbors(x, y):
            neighbors = []
            if x > 0:
                neighbors.append((x-1, y))
            if x < R-1:
                neighbors.append((x+1, y))
            if y > 0:
                neighbors.append((x, y-1))
            if y < C-1:
                neighbors.append((x, y+1))
            return neighbors
        
        def is_compass_neighbor(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2) == 1 and grid[x1][y1] != 0
        
        def calculate_average_skill_level(neighbors):
            if not neighbors:
                return 0
            total = sum(grid[nx][ny] for nx, ny in neighbors)
            return total / len(neighbors)
        
        interest_level = 0
        while True:
            active_competitors = [(x, y) for x in range(R) for y in range(C) if grid[x][y] != 0]
            eliminated = False
            
            for x, y in active_competitors:
                neighbors = get_neighbors(x, y)
                avg_skill_level = calculate_average_skill_level(neighbors)
                
                if neighbors and grid[x][y] < avg_skill_level:
                    grid[x][y] = 0
                    eliminated = True
                    
            interest_level += sum(grid[x][y] for x in range(R) for y in range(C))
            
            if not eliminated:
                break
        
        results.append(f"Case #{i+1}: {interest_level}")
    
    return results

# Example usage:
test_cases = [
    {'R': 1, 'C': 1, 'grid': [[15]]},
    {'R': 3, 'C': 9, 'grid': [[1]*9, [1]*9, [1]*9, [1]*9, [2]+[1]*7, [1]*9, [1]*9, [1]*9, [1]*9]},
    {'R': 1, 'C': 3, 'grid': [[6], [5], [3]]}
]

results = calculate_interest_level(3, test_cases)
for result in results:
    print(result)