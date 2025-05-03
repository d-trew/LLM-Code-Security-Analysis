Here's the Python code for your problem:


from math import factorial as f
MOD = 10**9 + 7
def inv(x):
    return pow(x, MOD-2, MOD)
fact = [f(i) % MOD for i in range(13)] + [0]*85
inv_fact = [inv(f(i)) % MOD for i in range(13)] + [0]*85
def choose(n, k):
    if k > n or k < 0: return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD
t = int(input())
for case in range(1, t+1):
    n = int(input())
    visibles = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        if visibles[i-1] == i:
            ans += choose(n, i) * pow(2, i*(n-i), MOD) % MOD
            ans %= MOD
        elif visibles[i-1] == i-1 and visibles[i-2] < i - 1:
            ans += choose(n, i) * (pow(2, i*(n-i), MOD)-1) % MOD
            ans %= MOD
    print("Case #%d: %d" % (case, ans))

This program uses dynamic programming to solve the problem. The `choose` function calculates combinations modulo 10^9+7. It first calculates factorials and their inverses up to n=12, then extends these lists by zeros for future use. For each test case, it checks the number of visible pancakes at each step. If all pancakes are visible or none are, we have `choose(n, i) * pow(2, i*(n-i), MOD) % MOD` possible cooking orders (where `pow(2, i*(n-i), MOD)` is the number of ways to arrange the visible pancakes). If exactly one pancake is visible at each step, we have `choose(n, i) * (pow(2, i*(n-i), MOD)-1) % MOD` possible cooking orders. The result is the sum of these possibilities modulo 10^9+7 for all i from 1 to n.