from random import randint

def bit_count(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

T = int(input())
for _ in range(T):
    record = ''.join([str(randint(0, 1)) for _ in range(8)])
    while bit_count(int(record, 2)) > 0:
        V = ''.join([str(randint(0, 1)) for _ in range(8)])
        r = randint(0, 7)
        record = ((int(record, 2) ^ (int(V, 2) << r)) & 0xff).to_bytes(1, 'big').decode()
    print('0' * 8 if int(record, 2) == 0 else '-1')