import heapq
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    D = list(map(int, input().split()))
    max_deliciousness = max(D)
    min_deliciousness = min(D)
    res = 0
    for d in D:
        if d >= max_deliciousness:
            res += 1
            max_deliciousness -= 1
        elif d <= min_deliciousness:
            res += 1
            min_deliciousness += 1
    print(f"Case #{t}: {res}")