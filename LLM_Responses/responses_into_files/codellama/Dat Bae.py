T = int(input())
for _ in range(T):
    N, B, F = map(int, input().split())
    bits = []
    for _ in range(F):
        bits.append(input())
    broken_workers = set()
    for i in range(len(bits)):
        result = input()
        if len(result) != N - B:
            break
        for j in range(N - B):
            if result[j] == '1':
                broken_workers.add(i)
    print(*sorted(broken_workers), sep=' ')