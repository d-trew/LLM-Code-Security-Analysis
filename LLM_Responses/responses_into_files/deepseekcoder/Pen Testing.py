import sys
from random import shuffle

def readline_int_list():
    return list(map(int, input().split()))

t, n, c = readline_int_list()
pens = [i for i in range(1, n+1)]
shuffle(pens)

ink_left = {}
for i in pens:
    ink_left[i] = 0 if i == n else 1

def write(pen):
    if pen in ink_left and ink_left[pen] > 0:
        ink_left[pen] -= 1
        return 1
    else:
        return 0

succeeded = 0
rounds = n * (n + 1) // 2
for _ in range(rounds):
    sys.stdout.write(' '.join(map(str, pens)) + '\n')
    sys.stdout.flush()
    result = readline_int_list()
    for i, pen in enumerate(pens):
        if write(pen) == result[i]:
            succeeded += 1
        else:
            ink_left[pen] = 0

sys.stdout.write(' '.join(map(str, [3, 4])) + '\n')
if succeeded >= c:
    sys.stdout.write('0\n')
else:
    sys.stdout.write('-1\n')