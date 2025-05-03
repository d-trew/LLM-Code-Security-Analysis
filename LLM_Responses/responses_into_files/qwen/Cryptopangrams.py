def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def decrypt(ciphertext, N):
    plaintext = [''] * len(ciphertext)
    for i in range(len(ciphertext)):
        prime_factors_list = [N]
        for j in range(i):
            prime_factors_list.append(ciphertext[j])
        product = 1
        for num in prime_factors_list:
            product *= num
        prime_index = (product - 2) % 26
        if prime_index < 10:
            plaintext[i] = chr(ord('A') + prime_index)
        else:
            plaintext[i] = chr(ord('a') + prime_index - 10)
    return ''.join(plaintext)

T = int(input())
for t in range(T):
    N, L = map(int, input().split())
    ciphertext = list(map(int, input().split()))
    print(f"Case #{t+1}: {decrypt(ciphertext, N)}")