def solve(K, N, X, T):
    # Create a list of tuples for each temperature measurement
    measurements = [(X[i], T[i]) for i in range(N)]
    
    # Initialize the minimum number of thermometers to K (the maximum possible)
    min_thermometers = K
    
    # Iterate over all possible combinations of thermometer locations
    for i in range(1 << N):
        # Create a list of temperature measurements that would be produced with this combination
        produced = [T[0]] + [next((t for x, t in sorted(measurements)[j:] if x > X[i-j]), T[-1]) 
                             for j in range(N)]
        
        # If the produced measurements match the input measurements, update the minimum number of thermometers
        if all(a == b for a, b in zip(produced, T)):
            min_thermometers = min(min_thermometers, bin(i).count("1"))
    
    return min_thermometers

T = int(input())
for tc in range(1, T + 1):
    K, N = map(int, input().split())
    X = list(map(int, input().split()))
    T = list(map(int, input().split()))
    print("Case #{}: {}".format(tc, solve(K, N, X, T)))