import math
p, q = 1, 1
MOD = 1000000007
def mul(a, b):
    return (a * b) % MOD
def power(a, k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        half = power(a, k // 2)
        return mul(half, half)
    else:
        return mul(a, mul(power(a, k - 1), MOD))
T = int(input())
for i in range(1, T + 1):
    M, K = map(int, input().split())
    ways = math.factorial(M * (M - 1) // 2)
    for _ in range(K - 1):
        ways //= (M - _ - 1) * (_ + 1)
    p *= ways
    q = power(q, M * (M - 1) // 2)
    print(f"Case #{i}: {mul(p, power(q, MOD - 2))}")