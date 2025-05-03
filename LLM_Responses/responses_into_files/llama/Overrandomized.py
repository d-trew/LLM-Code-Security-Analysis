import re
import random
from collections import defaultdict

T = int(input())
pattern = r'([A-Z]{10})\n(\d+)\n(.*)'
results = []

for _ in range(T):
    D = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
    U = 16
    M = [random.randint(1, U-1) for _ in range(104)]
    N = [random.randint(1, m) for m in M]
    R = [''.join([D[int(str(n)[i])] for i in range(len(str(n)))]) for n in N]

    print('Case #{}: {}'.format(_, D))