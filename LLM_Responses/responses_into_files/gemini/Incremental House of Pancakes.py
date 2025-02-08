def solve():
    L, R = map(int, input().split())
    i = 1
    while True:
        if L >= R:
            if L >= i:
                L -= i
            else:
                break
        else:
            if R >= i:
                R -= i
            else:
                break
        i += 1
    return i -1, L, R

T = int(input())
for i in range(1, T + 1):
    n, l, r = solve()
    print(f"Case #{i}: {n} {l} {r}")