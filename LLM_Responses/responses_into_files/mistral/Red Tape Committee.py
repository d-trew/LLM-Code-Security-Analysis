T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    Ps = list(map(float, input().split()))
    Ps.sort(reverse=True)
    total_prob = 0
    for i in range(K // 2):
        if Ps[i] > Ps[K - i - 1]:
            total_prob += (Ps[i] + Ps[K - i - 1]) / 2
        else:
            total_prob += min(Ps[i], Ps[K - i - 1])
    print(f"Case #{_+1}: {total_prob:.6f}")