from collections import Counter

def magnificent_arrangement(jugglers):
    pairs = []
    for i in range(len(jugglers) // 2):
        j1 = i * 2
        j2 = (i * 2) + 1
        pair = tuple(sorted([j1, j2]))
        pairs.append(pair)
    return ' '.join(map(str, [pair[0] + 1 for pair in pairs]))

T = int(input())
for t in range(T):
    N = int(input())
    jugglers = []
    for _ in range(N * 2):
        x, y = map(int, input().split())
        jugglers.append((x, y))
    arrangement = magnificent_arrangement(jugglers)
    print(f'Case #{t + 1}: {arrangement}')