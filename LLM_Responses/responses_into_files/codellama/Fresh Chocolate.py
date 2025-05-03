import math

T = int(input())
for i in range(T):
    N, P = map(int, input().split())
    G = list(map(int, input().split()))
    total_groups = len(set(G))
    if total_groups == 1:
        print("Case #{}: {}".format(i+1, total_groups))
        continue
    group_sizes = sorted(list(set(G)), reverse=True)
    max_groups = math.ceil(N / P)
    best_order = []
    for j in range(max_groups):
        for k in range(len(group_sizes)):
            if group_sizes[k] > 0:
                best_order.append(group_sizes[k])
                group_sizes[k] -= 1
    print("Case #{}: {}".format(i+1, len(best_order)))