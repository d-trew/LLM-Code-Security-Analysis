def solve_case(N, R, P, S):
    R = min(R, N)
    P = min(P, N - R)
    S = N - R - P
    res = []
    if R > 0:
        res.append('R' * (2 * R))
    if P > 0:
        res.append('P' * (2 * P))
    if S > 0:
        res.append('S' * (2 * S))
    return 'IMPOSSIBLE' if any(len(x) % 2 == 0 for x in res) else ''.join(sorted(res[0]))

T = int(input())
for _ in range(T):
    N, R, P, S = map(int, input().split())
    print('Case #{}: {}'.format(_, solve_case(N, R, P, S)))