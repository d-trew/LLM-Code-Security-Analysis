def solve():
    N, D = map(int, input().split())
    S, E = input().split()
    L = input().split()

    S_int = int(S, 16)
    E_int = int(E, 16)
    
    L_int = [int(x, 16) for x in L]
    
    total_pairs = N * (N - 1) // 2
    successful_pairs = 0

    for i in range(N):
        for j in range(i + 1, N):
            sum_hex = hex((L_int[i] + L_int[j]) % (16**D))[2:].upper()
            sum_int = int(sum_hex, 16)
            
            if len(sum_hex) < D:
                sum_hex = "0" * (D-len(sum_hex)) + sum_hex
                sum_int = int(sum_hex,16)
            
            if S_int <= sum_int <= E_int:
                successful_pairs += 1

    if total_pairs == 0:
        return "0/1"
    
    gcd_val = gcd(successful_pairs, total_pairs)
    return f"{successful_pairs // gcd_val}/{total_pairs // gcd_val}"

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")