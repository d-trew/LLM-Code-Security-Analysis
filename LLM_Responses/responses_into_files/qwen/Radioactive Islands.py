import math

def min_radiation_dose(N, A, B, C):
    total_radiation = 0
    
    for Ci in C:
        # Distance from the boat's starting point (-10, A) to the island (0, Ci)
        D_start = math.sqrt((-10)**2 + (A - Ci)**2)
        
        # Distance from the boat's ending point (10, B) to the island (0, Ci)
        D_end = math.sqrt((10)**2 + (B - Ci)**2)
        
        # Total radiation from this island
        total_radiation += 1 / D_start**2 + 1 / D_end**2
    
    return total_radiation

# Read input
T = int(input())
results = []

for i in range(1, T + 1):
    N, A, B = map(float, input().split())
    C = list(map(float, input().split()))
    
    # Calculate the minimum radiation dose for this test case
    min_dose = min_radiation_dose(N, A, B, C)
    
    # Store the result
    results.append(f"Case #{i}: {min_dose:.3f}")

# Print all results
for result in results:
    print(result)