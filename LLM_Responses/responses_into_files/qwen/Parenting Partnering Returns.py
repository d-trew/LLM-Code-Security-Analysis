def assign_activities(T, cases):
    results = []
    
    for i in range(T):
        N = cases[i][0]
        activities = sorted(cases[i][1:], key=lambda x: (x[0], -x[1]))
        
        Cameron = [False] * 24 * 60
        Jamie = [False] * 24 * 60
        
        for start, end in activities:
            if not any(Cameron[s:e] or Jamie[s:e] for s in range(start) for e in range(end)):
                Cameron[start:end] = True
            else:
                Jamie[start:end] = True
        
        if all(Cameron[start:end] or Jamie[start:end] for start, end in activities):
            results.append(f"Case #{i+1}: {''.join('C' if Cameron[s] else 'J' for s, e in activities)}")
        else:
            results.append(f"Case #{i+1}: IMPOSSIBLE")
    
    return results

# Example usage
T = 4
cases = [
    (3, [(1800, 2000), (1900, 2100), (2200, 2300)]),
    (3, [(60, 120), (90, 150), (120, 180)]),
    (3, [(100, 200), (150, 250), (200, 300)]),
    (4, [(60, 120), (180, 240), (300, 360), (420, 480)])
]

print(assign_activities(T, cases))