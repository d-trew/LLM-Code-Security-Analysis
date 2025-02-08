import itertools
from math import gcd

def solve():
    S, C = map(int, input().split())
    cards = []
    for _ in range(C):
        cards.append(input().split())

    max_num = -float('inf')
    max_den = 1

    for perm in itertools.permutations(cards):
        num = S
        den = 1
        for op, val in perm:
            if op == '+':
                num = num * den + val * den
                den = den
            elif op == '-':
                num = num * den - val * den
                den = den
            elif op == '*':
                num = num * val
                den = den
            elif op == '/':
                num = num * val
                den = den * val

        if den !=0:
          common = gcd(abs(num), abs(den))
          num //= common
          den //= common
          if den < 0:
              num *= -1
              den *= -1
          if (num / den) > max_num:
              max_num = num / den
              max_num_n = num
              max_num_d = den


    return str(max_num_n) + " " + str(max_num_d)

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")