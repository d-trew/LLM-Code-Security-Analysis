def solve():
    N, L = map(int, input().split())
    ciphertext = list(map(int, input().split()))

    primes = []
    num = 3
    count = 0
    while count < 26:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            count += 1
        num += 2

    
    def find_factors(n):
        factors = []
        i = 0
        while i < len(primes):
          if n % primes[i] == 0:
            factors.append(primes[i])
            n //= primes[i]
          else:
            i+=1
        return factors

    first_num_factors = find_factors(ciphertext[0])
    
    plaintext = ""
    plaintext += chr(ord('A') + primes.index(first_num_factors[0]))
    
    
    prev_factor = first_num_factors[1]
    plaintext += chr(ord('A') + primes.index(prev_factor))

    for i in range(1,len(ciphertext)):
        factors = find_factors(ciphertext[i])
        next_factor = factors[0] if factors[0] != prev_factor else factors[1]
        plaintext += chr(ord('A') + primes.index(next_factor))
        prev_factor = factors[1] if factors[0] != prev_factor else factors[0]


    return plaintext


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")