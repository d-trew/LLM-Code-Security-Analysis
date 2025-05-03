import random

T, N, B, P = map(int, input().split())

score = 0
for _ in range(T):
    towers = [0] * N
    for _ in range(N * B):
        D = int(input())
        i = min(range(1, N+1), key=lambda x: str(D) + str(towers[x-1]).zfill(B))
        if len(str(towers[i-1])) > B:
            print(-1)
            exit()
        towers[i-1] = 10 * towers[i-1] + D
    score += sum(int(''.join(map(str, reversed(tower)))) for tower in reversed(towers))

if score >= P:
    print(1)
else:
    print(-1)