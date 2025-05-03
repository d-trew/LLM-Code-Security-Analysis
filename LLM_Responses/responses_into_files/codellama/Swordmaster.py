T = int(input())
for _ in range(T):
    P, N = map(int, input().split())
    A = []
    D = []
    for i in range(N):
        ai, di = map(int, input().split())
        A.append((ai - 1) % P)
        D.append((di - 1) % P)
    swordmaster = True
    for a, d in zip(A, D):
        if (a + 1 == d and (a + 2) % P not in [x[0] for x in A[:i]] and (d + 1) % P not in [x[1] for x in D[:i]]) or \
           (a + 1 != d and a in [x[0] for x in A[:i]] and d in [x[1] for x in D[:i]]):
            swordmaster = False
            break
    print('Case #{}: {}'.format(_, 'YES' if swordmaster else 'NO'))