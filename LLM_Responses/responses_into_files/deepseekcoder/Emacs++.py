def solve(K, Q, P, Li, Ri, Pi):
    prefix_sum = [0] * (K + 1)
    for i in range(1, K + 1):
        if P[i - 1] == '(':
            prefix_sum[i] = prefix_sum[i - 1] + 1
        else:
            prefix_sum[i] = prefix_sum[i - 1] - 1
    min_time = 0
    for i in range(Q):
        S, E = Li[i], Ri[i]
        if Pi[S-1] == 3 or (Pi[E-1] == 2 and prefix_sum[E] > prefix_sum[S] - 2) \
                or (Pi[E-1] == 1 and abs(prefix_sum[E] - prefix_sum[S]) <= 1):
            min_time += E - S + 1
    return min_time

T = int(input())
for t in range(1, T+1):
    K, Q = map(int, input().split())
    P = input()
    Li, Ri, Pi = [], [], []
    for _ in range(K):
        li, ri, pi = map(int, input().split())
        Li.append(li)
        Ri.append(ri)
        Pi.append(pi)
    print("Case #{}: {}".format(t, solve(K, Q, P, Li, Ri, Pi)))