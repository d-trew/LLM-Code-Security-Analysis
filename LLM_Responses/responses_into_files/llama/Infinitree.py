import heapq

def distance(L, R, A, B):
    n = len(L)
    queue = [(0, 1)]
    visited = {1}
    parent = {1: None}

    while queue:
        d, node = heapq.heappop(queue)

        if node == A:
            return d
        if node == B:
            return d

        if L[node-1] != 0 and L[node-1] not in visited:
            heapq.heappush(queue, (d+1, L[node-1]))
            parent[L[node-1]] = node
            visited.add(L[node-1])
        if R[node-1] != 0 and R[node-1] not in visited:
            heapq.heappush(queue, (d+1, R[node-1]))
            parent[R[node-1]] = node
            visited.add(R[node-1])

    return -1

T = int(input())
for i in range(1, T+1):
    N, A, B = map(int, input().split())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    print('Case #{}: {}'.format(i, distance(L, R, A, B)))