T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    if C < N:
        print('IMPOSSIBLE')
    else:
        res = []
        for i in range(1, N+1):
            res.append(N-i+1)
        while len(res) > 0 and sum(range(1, len(res)+1)) <= C:
            j = len(res)
            res = res[:j//2][::-1] + res[j//2:]
        if sum(range(1, len(res)+1)) == C:
            print('Case #{}: {}'.format(_, ' '.join(map(str, res))))
        else:
            print('IMPOSSIBLE')