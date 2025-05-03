import random

t = int(input().split()[0])
w = int(input().split()[1])

for _ in range(t):
    game = list(range(1, 1022))
    while True:
        p = int(input())
        if p == -2 or p == -3:
            break
        q = random.randint(max(1, p-1010+1), min(p, len(game)-p-1010+1))
        print(q)