import math
import sys
from collections import defaultdict

MOD = 10 ** 9 + 7

def factorial(n):
    return math.factorial(n) % MOD

def inv_fact(n):
    fact = [1]
    inv = [1]
    for i in range(1, n+1):
        fact.append(fact[i-1]*i%MOD)
        inv.append(pow(fact[i], MOD-2, MOD))
    return inv[n]

def solve(vs):
    n = len(vs)
    max_v = max(vs)
    dp = [[0 for _ in range(max_v+1)] for _ in range(n+1)]
    for i, v in enumerate(vs[::-1]):
        for j in range(i, max_v+1):
            if j >= v:
                dp[i][j] = (dp[i+1][j] + dp[i][j-v]*factorial(n-i)*inv_fact(i)*inv_fact(n-i-j+v)) % MOD
    return sum(dp[0]) % MOD

def main():
    T = int(input())
    for _ in range(T):
        N = int(input().strip())
        vs = list(map(int, input().split()))
        print("Case #{}: {}".format(_+1, solve(vs)))

if __name__ == "__main__":
    main()


This program reads the number of test cases T and then iterates over each test case. For each test case, it reads the number of pancakes N and the corresponding visible values vs. It uses dynamic programming to calculate the number of ways to arrange the pancakes such that they result in the given visible values. Finally, it outputs the result for each test case modulo 10^9+7.