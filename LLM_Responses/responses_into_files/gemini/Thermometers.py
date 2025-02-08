def solve():
    K, N = map(int, input().split())
    X = list(map(float, input().split()))
    T = list(map(int, input().split()))

    unique_temps = len(set(T))
    
    return unique_temps


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")