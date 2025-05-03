Here's the Python code that will solve this problem based on your description:


import sys
from fractions import gcd
input = sys.stdin.readline

def lcm(a, b):
    return a * b // gcd(a, b)

def solve():
    n, m = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(n)]
    
    min_packages = []
    max_servings = 0
    
    for i in range(1 << m):
        total = 1
        for j in range(m):
            if (i & (1 << j)):
                total = lcm(total, ingredients[j][1])
                
        min_packages.append((sum(ingredients[j][0] * (total // ingredients[j][1]) for j in range(m) if (i & (1 << j))), total))
        
    min_packages.sort()
    
    dp = [0] * len(min_packages)
    for i in range(len(min_packages)):
        dp[i] = 1 + max((dp[j] for j in range(i) if min_packages[j][1] <= min_packages[i][1]), default=0)
        max_servings = max(max_servings, dp[i])
        
    print(max_servings)
    
t = int(input())
for i in range(1, t + 1):
    print("Case #", i, ": ", sep='', end='')
    solve()