import random

def quantum_fluctuation(bit):
    possibilities = [bit, not bit]
    return random.choice(possibilities)

def get_bit(b):
    return quantum_fluctuation(bits[b-1])

T, B = map(int, input().split())
for _ in range(T):
    bits = list(map(lambda x: True if x == '1' else False, input()))
    for i in range(min(B, 150)):
        get_bit(i+1)
    print(''.join(['1' if bit else '0' for bit in bits]))