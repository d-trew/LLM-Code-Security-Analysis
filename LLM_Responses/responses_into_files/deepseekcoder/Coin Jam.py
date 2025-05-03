from sympy import *
import random

def generate_jamcoin(n):
    return bin(random.randint(2**(n-1) + 1, 2**n - 1))[2:]

def find_divisor(s):
    for i in range(2, int(sqrt(int(s, 2)))+1):
        if int(s, 2) % i == 0:
            return i
    return None

def generate_jamcoins(n, j):
    jamcoins = []
    while len(jamcoins) < j:
        s = generate_jamcoin(n)
        divisors = [find_divisor(s[i-1:] + '0') for i in range(1, n+1)]
        if all(d is not None for d in divisors):
            jamcoins.append((s, divisors))
    return jamcoins

def main():
    t = 1  # number of test cases
    for case_no in range(1, t + 1):
        n, j = map(int, input().split())
        print('Case #{}:'.format(case_no))
        for jamcoin, divisors in generate_jamcoins(n, j):
            print(jamcoin + ' ' + ' '.join(map(str, divisors)))

if __name__ == "__main__":
    main()