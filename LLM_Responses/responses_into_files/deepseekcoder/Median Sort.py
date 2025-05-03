T = int(input())
for _ in range(T):
    N = int(input())
    Q = int(input()) * T
    order = [-1] * N
    queries = []
    for _ in range(Q):
        i, j, k = map(int, input().split())
        queries.append((i, j, k))
    query_count = 0
    left = 0
    right = N - 1
    while query_count < Q:
        if left + 1 <= right - 1:
            mid = (left + right) // 2
            order[mid] = query_count
            query_count += 1
            queries[query_count-1] = (min(order), mid, max(order))
            for i in range(3):
                if queries[query_count][i] == min(order):
                    left = mid
                elif queries[query_count][i] == mid:
                    continue
                else:
                    right = mid
        else:
            order[left] = query_count
            query_count += 1
            for i in range(3):
                if queries[query_count-1][i] == left:
                    left += 1
                elif queries[query_count-1][i] == right:
                    right -= 1
    print(' '.join(map(str, order)))