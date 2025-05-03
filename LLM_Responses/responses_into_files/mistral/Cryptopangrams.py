import math
from sympy import isprime

def encrypt(n, p):
    primes = [2] + list(filter(isprime, range(3, n, 2)))
    return [primes[i-1]*primes[i%len(primes)] for i in range(1, len(p))]

def decrypt(n, ciphertext):
    primes = [2] + list(filter(isprime, range(3, n, 2)))
    plaintext_length = len(ciphertext) + 1
    plaintext = ['A' + chr(ord('A')+i) for i in range(plaintext_length)]
    products = ciphertext
    for i in range(plaintext_length - 2, 0, -1):
        product = 1
        for j in range(i-1, i-plaintext_length, -plaintext_length):
            product *= primes[j]
        plaintext[i] = chr((products[i-1]*product**(-1) - products[i-plaintext_length]) % n + ord('A'))
    return ''.join(plaintext)

def solve():
    T = int(input())
    for _ in range(T):
        n, L = map(int, input().split())
        ciphertext = list(map(int, input().split()))
        print(f'Case #{_ + 1}: {decrypt(n, ciphertext)}')

solve()


This code reads the test cases from standard input and outputs the decrypted messages to standard output. The `encrypt` function calculates the ciphertext given the prime number N and plaintext message, while the `decrypt` function recovers the plaintext message from the given ciphertext and prime number N.