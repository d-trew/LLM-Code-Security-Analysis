import math

def next_power_of_two(n):
    return int(math.pow(2, math.ceil(math.log2(n))))

def check_jamcoin(jamcoin, n):
    for i in range(2, 11):
        base = str(i)
        value = int(jamcoin, base)
        for j in range(2, value + 1):
            if value % j == 0:
                return True
    return False

def generate_jamcoin(n, j):
    while True:
        jamcoin = ''.join([str(random.randint(0, 1)) for _ in range(n)])
        if check_jamcoin(jamcoin, n) and not any([jamcoin == jam for jam in jams]):
            jams.append(jamcoin)
            if len(jams) == j + 1:
                break

jams = []
n, j = int(input()), int(input())
for i in range(1, j + 1):
    print(f"Case #{i}: {generate_jamcoin(n, j)}")