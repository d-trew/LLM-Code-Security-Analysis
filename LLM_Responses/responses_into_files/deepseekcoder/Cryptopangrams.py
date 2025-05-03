def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    for i in range(3,int(n**0.5)+1,2): 
        if n%i == 0: 
            return False    
    return True

def decrypt_pangram(ciphertext, primes):
    plain = ""
    for i in range(len(ciphertext)-1):
        product = ciphertext[i] * ciphertext[i+1]
        for char, prime in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", primes):
            if product == prime: 
                plain += char
                break
    return plain

def solve():
    T = int(input())
    for tc in range(1, T+1):
        N, L = map(int, input().split())
        ciphertext = list(map(int, input().split()))
        
        primes = [n for n in range(N) if is_prime(n)][25:]  # get the first 26 odd prime numbers
        plaintext = decrypt_pangram(ciphertext, primes)
        
        print("Case #{}: {}".format(tc, plaintext))

solve()