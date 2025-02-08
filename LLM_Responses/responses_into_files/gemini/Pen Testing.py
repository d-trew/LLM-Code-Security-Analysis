T, N, C = map(int, input().split())
pens = [[i + 1 for i in range(N)] for _ in range(T)]
ink_levels = [[0 for _ in range(N)] for _ in range(T)]

for i in range(N):
    query = [pens[j][0] if len(pens[j]) > 0 else 0 for j in range(T)]
    print(*query)
    result = list(map(int, input().split()))
    for j in range(T):
        if query[j] != 0:
            ink_levels[j][query[j]-1] += result[j]
            if result[j] == 0:
                pens[j].pop(0)

print(*([0] * T))

ans = []
for i in range(T):
    best_sum = -1
    best_pair = (-1,-1)
    for j in range(N):
        for k in range(j+1,N):
            cur_sum = ink_levels[i][j] + ink_levels[i][k]
            if cur_sum > best_sum:
                best_sum = cur_sum
                best_pair = (j+1,k+1)
    ans.extend(best_pair)

print(*ans)