import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = []
num = 2
while len(primes) < 26:
    if is_prime(num):
        primes.append(num)
    num += 1

def prime_product(n, i):
    return n * primes[i]

def decrypt(ciphertext, N):
    plaintext = ""
    for i in range(len(ciphertext)):
        if i == 0:
            plaintext += chr((primes.index(N // ciphertext[i]) + ord('A')) % 26)
        else:
            prime_product_divisor = N // ciphertext[i]
            for j in range(len(primes)):
                if primes[j] <= prime_product_divisor and (N % ciphertext[i]) % primes[j] == 0:
                    plaintext += chr((primes.index(prime_product_divisor // primes[j]) + ord('A')) % 26)
                    break
    return plaintext

T = int(input())
for i in range(1, T+1):
    N, L = map(int, input().split())
    ciphertext = list(map(int, input().split()))
    plaintext = decrypt(ciphertext[:L], N)
    print("Case #{}: {}".format(i, plaintext))