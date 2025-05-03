from math import factorial

MOD = 10**9 + 7

def mod_inverse(a, m):
    return pow(a, m - 2, m)

def comb(n, k, p):
    if k > n:
        return 0
    num = den = 1
    for i in range(k):
        num = num * (n - i) % p
        den = den * (i + 1) % p
    return num * mod_inverse(den, p) % p

def count_ways(M, K):
    n = M * (M - 1) // 2
    if K == 1:
        return 1
    if K > n or K < 1:
        return 0
    ways = 0
    for i in range(K):
        ways += comb(n, i, MOD)
        ways %= MOD
    return ways * mod_inverse(comb(M - 1, K - 1, MOD), MOD) % MOD

def solve():
    T = int(input())
    results = []
    for t in range(1, T + 1):
        M, K = map(int, input().split())
        result = count_ways(M, K)
        results.append(f"Case #{t}: {result}")
    return '\n'.join(results)

print(solve())