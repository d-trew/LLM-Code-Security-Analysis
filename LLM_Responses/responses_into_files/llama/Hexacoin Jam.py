T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    S, E = input(), input()
    L = [input() for _ in range(N)]
    hexacoins_found = 0
    for i in range(N):
        for j in range(i+1, N):
            a, b = int(L[i], 16), int(L[j], 16)
            if (a + b) % (16**D) < (int(S, 16)) or (a + b) % (16**D) > (int(E, 16)):
                continue
            hexacoins_found += 1
    probability = hexacoins_found / (N * (N-1) // 2)
    print(f"Case # {_+1}: {probability:.0f} {1/(16**D):.0f}")