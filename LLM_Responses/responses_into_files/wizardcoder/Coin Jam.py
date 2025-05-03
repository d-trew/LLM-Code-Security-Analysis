def generate_jamcoin(N, J):
    for i in range(J + 1):
        jamcoin = str(i) * N
        divisors = []
        for base in range(2, 11):
            jamcoin_base = int(jamcoin, base)
            for j in range(2, jamcoin_base + 1):
                if jamcoin_base % j == 0 and all([j % k != 0 for k in range(2, 10)]):
                    divisors.append(j)
        if len(divisors) >= 9:
            print("Case #", i + 1, ":", jamcoin, *divisors[:9])
generate_jamcoin(32, 500)