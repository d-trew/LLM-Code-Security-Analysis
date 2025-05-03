def reversort(n, c):
    if n * (n - 1) // 2 < c or c % 2 != n % 2:
        return "IMPOSSIBLE"
    lst = list(range(1, n + 1))
    res = []
    for i in range(n - 1):
        j = min(c - (i * (i + 1) // 2), ((n - i) * (n - i - 1) // 2) + i)
        c -= j - i
        lst[i:j] = reversed(lst[i:j])
    return ' '.join(map(str, lst))

t = int(input())
for case in range(1, t + 1):
    n, c = map(int, input().split())
    print("Case #{}: {}".format(case, reversort(n, c)))