from math import prod
from sys import stdin
from itertools import combinations

def solve():
    primes = list(map(int,stdin.readline().split()))
    dp1 = [0]*(1<<len(primes))
    dp2 = [0]*(1<<len(primes))
    total = 1<<len(primes)
    for mask in range(total):
        sub_set = [primes[i] for i in range(len(primes)) if (mask & 1<<i)!=0]
        dp1[mask] = sum(sub_set) if sub_set else 0
        dp2[mask] = prod(sub_set) if sub_set else 1
    dp = [[(dp1[a^b],dp2[a^b]) for b in range(total)] for a in range(total)]
    for c in reversed(range(len(primes))):
        for mask in range(1<<c):
            dp[mask][0] = max((dp1[mask],dp2[mask]), key=lambda x:abs(x[0]-x[1]))
            dp[mask|1<<c][0] = max((dp1[mask|1<<c],dp2[mask|1<<c]), key=lambda x:abs(x[0]-x[1]))
    for c in range(1,len(primes)):
        for mask in range(total):
            dp[mask][c%2] = max((dp1[mask],dp2[mask]), (dp1[mask|1<<c]+dp2[mask^1<<c],dp2[mask|1<<c]-dp1[mask^1<<c])) if c%2==0 else \
                            max((dp1[mask],dp2[mask]), (dp1[mask|1<<c]-dp2[mask^1<<c],dp2[mask|1<<c]+dp1[mask^1<<c]))
    return dp[0][len(primes)%2-1][0] if len(primes) else 0

T = int(stdin.readline())
for t in range(1, T + 1):
    print("Case #{}: {}".format(t, solve()))