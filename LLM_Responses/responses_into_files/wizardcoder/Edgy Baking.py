T = int(input())
for i in range(1, T+1):
    N, P = map(int, input().split())
    W_H = []
    for j in range(N):
        W_H.append(list(map(int, input().split()))
    W = [w[0] for w in W_H]
    H = [h[1] for h in W_H]
    perimeter_sum = sum([2*(w+h) for w, h in zip(W, H)]))