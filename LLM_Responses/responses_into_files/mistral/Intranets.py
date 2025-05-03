from math import factorial, gcd
from collections import defaultdict
import sys
 MOD = 10 ** 9 + 7

def mod_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if (b == 1):
        return 1 % MOD
    while (a > 1):
        q = a // b
        x0, a = a % b, b
        b, a = b % a, a
        x1, b = b, a
    if (x1 < 0):
        x1 += b0
    return x1 % MOD

def solve(m, k):
    links = ((i * (m - i)) // 2 for i in range(1, m + 1))
    active_links = set()
    link_count = defaultdict(int)
    for link in links:
        link_count[link] += 1

    for _ in range(k):
        link = max(link_count, key=link_count.get)
        active_links.add(link)
        link_count[link] -= 1

    total = factorial(len(links))
    active = len(active_links)
    if (active > k or active < m - k):
        print("Case #{}: 0".format(sys.argv[1]))
        return

    ways = 1
    for link in links:
        if link not in active_links:
            ways *= link_count[link]
            ways %= MOD

    ans = (ways * mod_inv(total, MOD)) % MOD
    print("Case #{}: {}".format(sys.argv[1], ans))

if __name__ == "__main__":
    for _ in range(int(input())):
        m, k = map(int, input().split())
        solve(m, k)


This Python code solves the problem described. It first defines some constants and helper functions to compute the modular inverse of a number. The `solve()` function takes the number of machines (m) and target number of intranets (k) as arguments, initializes variables for active links, total possible link configurations, and the number of active links. It then iteratively selects the highest priority active link until there are either k or m-k active links. If the number of active links is not equal to k or m-k, it outputs 0 as the answer. Otherwise, it computes the number of ways to assign priorities such that exactly active links are active and the remaining links are not, and returns the result modulo MOD. The main part of the code reads the test cases from standard input and calls `solve()` for each case.