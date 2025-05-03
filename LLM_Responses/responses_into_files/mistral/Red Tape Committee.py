import fractions
import sys
from itertools import combinations

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, K = map(int, sys.stdin.readline().split())
        if K % 2 != 0:
            print("Error Case #{}: Bad input.".format(_ + 1))
            continue
        probs = list(map(float, sys.stdin.readline().split()))
        max_prob = fractions.Fraction(0)
        for combo in combinations(probs, K // 2):
            prob = 0
            for xor in [sum(a == b for a, b in zip(combo, reversed(combo))): i < K // 2 for i in range(K // 2)]:
                if xor == 1:
                    prob += (1 - prod(map(abs, combo))) / 2**(K//2)
                elif xor == 0:
                    prob += prod(combo) / 2**(K//2)
            max_prob = max(max_prob, prob)
        print("Case #{}: {:.6f}".format(_ + 1, max_prob))

solve()