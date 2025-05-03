def pyramidification_cost(S, P):
    H = [0] + P
    cost = 0
    for i in range(1, S):
        if H[i] < H[i-1]:
            diff = H[i-1] - H[i]
            cost += diff
            H[i] += diff
    return cost

T = int(input())
for t in range(1, T+1):
    S = int(input())
    P = list(map(int, input().split()))
    total_cost = 0
    for L in range(S-3):
        for R in range(min(S-L-3, L+1)):
            H = [0] + P[L+1:L+R+1]
            cost = pyramidification_cost(len(H), H)
            total_cost += cost
    print(f"Case #{t}: {total_cost % 1000000007}")