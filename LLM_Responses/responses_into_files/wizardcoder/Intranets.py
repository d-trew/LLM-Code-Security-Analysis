import random
from fractions import Fraction
from functools import reduce
import operator

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def mod_inverse(n, p):
    for i in range(p - 2, -1, -1):
        if (n * i) % p == 1:
            break
    else:
        raise ValueError("Inverse doesn't exist.")
    return i

def count_intranets(M, K):
    total = reduce(operator.mul, range(1, M + 1), 1)
    active_links = (M * (M - 1)) // 2
    possible_priorities = [(i, j) for i in range(1, M + 1) for j in range(i+1, M + 1)]
    active_combinations = [Fraction(sum([1 if random.randint(1, active_links) <= k else 0 for k in range(active_links)]) == K - 1 for _ in range(M * (M-1) // 2)]
    count = sum(active_combinations)
    return count / total

def compute_probability(M, K):
    total = reduce(operator.mul, range(1, M + 1), 1)
    active_links = (M * (M - 1)) // 2
    possible_priorities = [(i, j) for i in range(1, M + 1) for j in range(i+1, M + 1)]
    active_combinations = [Fraction(sum([1 if random.randint(1, active_links) <= k else 0 for k in range(active_links)]) == K - 1 for _ in range(total)]
    count = sum(active_combinations)
    probability = Fraction(count, total)
    return (probability.numerator * mod_inverse(probability.denominator, 10**9 + 7)) % (10**9 + 7)

def main():
    T = int(input())
    for i in range(T):
        M, K = map(int, input().split())
        print("Case #{}: {}".format(i+1, compute_probability(M, K))

if __name__ == "__main__":
    main()