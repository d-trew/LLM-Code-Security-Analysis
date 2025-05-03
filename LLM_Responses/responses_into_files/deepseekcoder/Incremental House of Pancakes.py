T = int(input())
for i in range(1, T+1):
    L, R = map(int, input().split())
    l, r = 0, 0
    customers = 0
    while L > 0 and R > 0:
        if L >= R:
            L -= min(L, R)
            r += 1
        else:
            R -= min(L, R)
            l += 1
        if min(L, R) == 0:
            break
        customers += 1
    print(f'Case #{i}: {customers} {L} {R}')