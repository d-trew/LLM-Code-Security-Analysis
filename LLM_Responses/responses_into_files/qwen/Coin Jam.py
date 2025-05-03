def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_nontrivial_divisor(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and i != n // i:
            return i
    return None

def generate_jamcoin(length, num_jamcoins):
    jamcoins = []
    while len(jamcoins) < num_jamcoins:
        jamcoin = '1' + ''.join('0' if i % 2 == 0 else '1' for i in range(1, length - 1)) + '1'
        valid = True
        for base in range(2, 11):
            value = int(jamcoin, base)
            if is_prime(value) or find_nontrivial_divisor(value) is None:
                valid = False
                break
        if valid:
            jamcoins.append((jamcoin, [find_nontrivial_divisor(int(jamcoin, base)) for base in range(2, 11)]))
    return jamcoins

T = int(input())
for t in range(1, T + 1):
    N, J = map(int, input().split())
    jamcoins = generate_jamcoin(N, J)
    print(f"Case #{t}:")
    for jamcoin, divisors in jamcoins:
        print(jamcoin, *divisors)