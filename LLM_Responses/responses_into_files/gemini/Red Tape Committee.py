def solve():
    N, K = map(int, input().split())
    P = list(map(float, input().split()))

    max_tie_prob = 0.0

    for i in range(1 << N):
        committee = []
        count = 0
        for j in range(N):
            if (i >> j) & 1:
                committee.append(P[j])
                count += 1
        
        if count == K:
            tie_prob = 0.0
            for j in range(1 << K):
                yes_votes = 0
                for k in range(K):
                    if (j >> k) & 1:
                        yes_votes += 1
                
                if yes_votes == K // 2:
                    prob = 1.0
                    for k in range(K):
                        if (j >> k) & 1:
                            prob *= committee[k]
                        else:
                            prob *= (1 - committee[k])
                    tie_prob += prob

            max_tie_prob = max(max_tie_prob, tie_prob)

    return max_tie_prob

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")