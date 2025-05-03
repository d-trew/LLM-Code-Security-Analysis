import heapq

def jelly_saver(N, kids, sweets):
    heap = []
    for i in range(1, N+2):
        for j in range(N+1):
            if i == 1:
                continue
            dist = ((kids[j-1][0] - sweets[i-1][0]) ** 2 + (kids[j-1][1] - sweets[i-1][1]) ** 2) ** 0.5
            heapq.heappush(heap, (dist, i))
    for _ in range(N):
        _, jelly = heapq.heappop(heap)
        print(f"Case #{N+1}: POSSIBLE")
        for i in range(1, N+1):
            if i == 1:
                print(f"{i} {jelly}")
            else:
                while True:
                    dist, j = heapq.heappop(heap)
                    if j != jelly:
                        print(f"{i} {j}")
                        break
    return

T = int(input())
for t in range(T):
    N = int(input())
    kids = []
    for _ in range(N):
        x, y = map(int, input().split())
        kids.append((x, y))
    sweets = []
    for _ in range(N+1):
        x, y = map(int, input().split())
        sweets.append((x, y))
    jelly_saver(N, kids, sweets)