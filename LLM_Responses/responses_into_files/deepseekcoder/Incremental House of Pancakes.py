T = int(input())
for case_num in range(1, T + 1):
    L, R = map(int, input().split())
    n = 0
    while min(L, R) >= n+1:
        if L > R:
            L -= n+1
            n += 1
        else:
            R -= n+1
            n += 1
    print(f"Case #{case_num}: {n} {L} {R}")