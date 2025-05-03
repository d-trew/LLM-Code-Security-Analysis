import sys
from math import comb, gcd
mod = 1000000007

def pyramidify(stacks):
    n = len(stacks)
    max_height = max(stacks)
    min_height = min(stacks)
    cost = 0
    for i in range(n - 2, -1, -1):
        if stacks[i] < min_height:
            cost += (min_height - stacks[i]) * comb(n - i - 1, i + 1) % mod
    return cost

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        S = int(sys.stdin.readline())
        stacks = list(map(int, sys.stdin.readline().split()))
        L, R = 0, min(S - 3, S // 2)
        while L + R > S - 3:
            R -= 1
        cost_sum = 0
        for l in range(L + 1):
            stacks_l = stacks[:l] + [stacks[l] + R] + stacks[l+1:]
            cost = pyramidify(stacks_l)
            cost_sum += cost
        for r in range(R + 1):
            stacks_r = stacks[:S - r - L - 1] + [stacks[-1] + L] + stacks[S - r - L:]
            cost = pyramidify(stacks_r)
            cost_sum += cost
        print('Case #{}: {}'.format(_+1, cost_sum % mod))

solve()


This Python program takes input as test cases, each containing the number of stacks and their heights. It computes and prints the sum of pyramidification costs over all valid choices of L and R, modulo 109 + 7. The `pyramidify()` function calculates the cost of adding pancakes to a given sequence of stacks so that they have the pyramid property, while the `solve()` function reads input and computes the answer for each test case.