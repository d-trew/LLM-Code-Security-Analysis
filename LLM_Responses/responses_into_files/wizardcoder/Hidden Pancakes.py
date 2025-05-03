import math
MOD = 10**9 + 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solve():
    test_cases = int(input())
    
    for i in range(1, test_cases + 1):
        n = int(input())
        visible_pancakes = list(map(int, input().split()))
        
        result = 1
        for j in range(n - 2, -1, -1):
            if visible_pancakes[j] > visible_pancakes[j + 1]:
                result *= lcm(visible_pancakes[j], result) // visible_pancakes[j + 1]
        
        print("Case #{}: {}".format(i, result % MOD))

if __name__ == "__main__":
    solve()