def min_thermometers(K, N, X, T):
    # Initialize the number of thermometers to 1 (minimum possible)
    num_thermometers = 1
    
    # If there's only one temperature measurement, no need for additional thermometers
    if N == 1:
        return num_thermometers
    
    # Iterate through each pair of temperature measurements
    for i in range(N):
        # Check if the current thermometer can cover the next segment
        if X[i + 1] - X[i] > K / num_thermometers:
            # If not, increment the number of thermometers
            num_thermometers += 1
    
    return num_thermometers

# Read input
T = int(input())
results = []

for t in range(1, T + 1):
    K, N = map(int, input().split())
    X = list(map(float, input().split()))
    T = list(map(int, input().split()))
    
    # Calculate the minimum number of thermometers for the current test case
    min_temp_thermometers = min_thermometers(K, N, X, T)
    
    # Store the result
    results.append(f"Case #{t}: {min_temp_thermometers}")

# Print all results
for result in results:
    print(result)