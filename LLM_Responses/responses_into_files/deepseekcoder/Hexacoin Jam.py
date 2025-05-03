def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def hex_to_dec(hex_num):
    return int(hex_num, 16)

def dec_to_hex(dec_num):
    return format(dec_num, 'X')

def calc_probability(N, D, S, E, L):
    count = 0
    total = (16 ** D) // 2
    for i in range(16 ** D):
        num1 = dec_to_hex(i).zfill(D)
        for j in range(16 ** D):
            num2 = dec_to_hex(j).zfill(D)
            if hex_to_dec(num1) + hex_to_dec(num2) % (16 ** D) >= S and hex_to_dec(num1) + hex_to_dec(num2) % (16 ** D) <= E:
                count += 1
    g = gcd(count, total)
    return f"{count//g}/{total//g}"

T = int(input())
for t in range(1, T + 1):
    N, D = map(int, input().split())
    S, E = map(lambda x: hex_to_dec(x), input().split())
    L = [hex_to_dec(num) for num in input().split()]
    print(f"Case #{t}: {calc_probability(N, D, S, E, L)}")