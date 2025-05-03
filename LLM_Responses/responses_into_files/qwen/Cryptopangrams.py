def decrypt_pangram(N, ciphertext):
    from sympy import primerange

    primes = list(primerange(2, N + 1))
    prime_dict = {chr(i + ord('A')): primes[i - ord('A')] for i in range(26)}

    plaintext = []
    current_product = 1
    for value in ciphertext:
        current_product *= value
        for letter, prime in prime_dict.items():
            if current_product % prime == 0:
                plaintext.append(letter)
                current_product //= prime
                break

    return ''.join(plaintext)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        N = int(data[index])
        L = int(data[index + 1])
        ciphertext = list(map(int, data[index + 2:index + 2 + L]))
        index += 2 + L

        plaintext = decrypt_pangram(N, ciphertext)
        results.append(f"Case #{_ + 1}: {plaintext}")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()