def solve_cake_problem(test_cases):
    results = []
    
    for test_case in test_cases:
        R, C = map(int, test_case[0].split())
        cake = test_case[1:]
        
        # Create a dictionary to store the positions of each letter
        letter_positions = {}
        for r in range(R):
            for c in range(C):
                if cake[r][c] != '?':
                    if cake[r][c] not in letter_positions:
                        letter_positions[cake[r][c]] = []
                    letter_positions[cake[r][c]].append((r, c))
        
        # Assign each letter to a rectangle
        assigned_letters = {}
        for letter, positions in letter_positions.items():
            min_r = max_r = positions[0][0]
            min_c = max_c = positions[0][1]
            for r, c in positions:
                if r < min_r: min_r = r
                if r > max_r: max_r = r
                if c < min_c: min_c = c
                if c > max_c: max_c = c
            assigned_letters[letter] = (min_r, max_r, min_c, max_c)
        
        # Create the result grid
        result_grid = [[ '?' for _ in range(C)] for _ in range(R)]
        for letter, (min_r, max_r, min_c, max_c) in assigned_letters.items():
            for r in range(min_r, max_r + 1):
                for c in range(min_c, max_c + 1):
                    result_grid[r][c] = letter
        
        # Add the result to the results list
        results.append(f"Case #{test_case[0].split()[2]}:")
        for row in result_grid:
            results.append(''.join(row))
    
    return results

# Example usage:
test_cases = [
    ("3 3\nA?C\nB?D\nE?F",),
    ("2 2\nX?\nY?",)
]
results = solve_cake_problem(test_cases)
for result in results:
    print(result)