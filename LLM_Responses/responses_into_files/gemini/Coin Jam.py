def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve():
    N, J = map(int, input().split())
    
    jamcoins = []
    count = 0
    
    for i in range(2**(N-1) + 1, 2**N):
        binary = bin(i)[2:].zfill(N)
        if binary[0] == '0' or binary[-1] == '0':
            continue

        divisors = []
        is_jamcoin = True
        for base in range(2, 11):
            num = int(binary, base)
            divisor = None
            for j in range(2, int(num**0.5) + 1):
                if num % j == 0:
                    divisor = j
                    break
            if divisor is None:
                is_jamcoin = False
                break
            divisors.append(divisor)

        if is_jamcoin:
            jamcoins.append((binary, divisors))
            count += 1
            if count == J:
                break

    return jamcoins

T = 1
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}:")
    for jamcoin, divisors in result:
        print(jamcoin, *divisors)