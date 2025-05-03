import math
import sys
from math import gcd
modulo = 1000000007

def count_divisible(s, d):
    l = len(s)
    total = (1 << l - 1)
    count = 0

    for i in range(total + 1):
        substrings = bin(i)[2:].zfill(l)
        is_divisible = True

        for j in range(len(substrings) - 1):
            a, b = int(substrings[j], 2), int(substrings[j + 1], 2)
            if gcd(a, d) == 1 and gcd(b, d) == 1:
                is_divisible = False
                break

        if is_divisible:
            count += 1

    return count % modulo

T = int(sys.stdin.readline())
for _ in range(T):
    s, d = sys.stdin.readline().strip().split()
    print(f'Case #{_+1}: {count_divisible(s, int(d))}')


This code reads the number of test cases from the standard input and then iterates through each test case. For each test case, it calculates the number of divisible divisions using a binary search approach. It first calculates the total number of possible divisions by computing 2^(length of S) - 1. Then, for each potential division, it checks if the pair of consecutive substrings is divisible by D. If all pairs are divisible, it increments the count. Finally, it returns the result modulo the prime 10^9+7 (1000000007).