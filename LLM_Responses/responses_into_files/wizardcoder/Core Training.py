import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solve(N, K, P):
    lcm_value = 1
    for i in range(1, N + 1):
        lcm_value = lcm(lcm_value, i)
    
    total_units = lcm_value * N
    max_probability = 0.0
    for units in range(total_units + 1):
        core_success_count = sum([math.floor((P[i] * (units + i)) / lcm_value) - P[i] * min(units, i) for i in range(N)])
        if core_success_count >= K:
            probability = 1 - ((1 - sum([math.pow(1 - P[i], units // lcm_value)) for i in range(N)]).prod())
            max_probability = max(max_probability, probability)
    return max_probability

T = int(input())
for case in range(1, T + 1):
    N, K = map(int, input().split())
    U = float(input())
    P = list(map(float, input().split()))
    
    result = solve(N, K, P)
    print("Case #{}: {:.6f}".format(result))