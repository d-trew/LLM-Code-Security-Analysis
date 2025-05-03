from math import gcd
import itertools

def find_jamcoin(n):
    jamcoins = set()
    divisors = set()

    for a in range(1, n // 2 + 1):
        for b in range(a + 1, n // 2 + 1):
            num = (a << n - b) | (b << b)
            if is_prime(num): continue
            divisors.add(num)
            jamcoins.add(bin(num)[2:])
    for j in range(len(jamcoins)):
        jamcoin = list(itertools.islice(jamcoins, j))[0]
        divisors[(2,)] = gcd(divisors[(2,)], int(jamcoin, 2))
        for i in range(3, 11):
            divisors[(i,)] = gcd(divisors[(i,)], int(jamcoin, i))
        print("Case #1:")
        print(f"{jamcoin} {', '.join(str(d) for d in divisors)}")

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): return False
    root = int(n ** 0.5) + 1
    for i in range(3, root, 2):
        if n % i == 0: return False
    return True

find_jamcoin(16)
find_jamcoin(32)


This script generates jamcoins of length N and their corresponding divisors for each base from 2 to 10, as described in the problem statement. It uses a set to store generated jamcoins and their divisors. The `is_prime()` function checks if a number is prime or not.