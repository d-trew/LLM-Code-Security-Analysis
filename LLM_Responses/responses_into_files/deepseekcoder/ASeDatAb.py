T = int(input())
for _ in range(T):
    V = input()
    N = 0
    while N < 300:
        r = int((8 * (2**31 - 1)) % len(V))
        V = str(format(int(V, 2) ^ (2**r), '08b'))
        N = bin(int(V, 2)).count('1')
        print(V)
    if N == 0:
        break
else:
    print(-1)