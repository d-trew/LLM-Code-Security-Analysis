import heapq
def max_lead(metals, relations, treasury):
    graph = [[] for _ in range(metals+1)]
    for i in range(1, metals+1):
        x, y = relations[i-1]
        graph[x].append((y, 1))
        graph[y].append((x, 1))
    
    dp = [0]*(metals+1)
    for i in range(1, metals+1):
        if treasury[i-1] > 0:
            heap = []
            heapq.heappush(heap, (-treasury[i-1], i))
            while heap:
                curr_lead, node = heapq.heappop(heap)
                curr_lead *= -1
                if dp[node] < curr_lead:
                    dp[node] = curr_lead
                for next_node, cost in graph[node]:
                    next_lead = (curr_lead+cost-1)//cost
                    if treasury[next_node-1]-dp[next_node] >= next_lead:
                        heapq.heappush(heap, (-next_lead, next_node))
    return dp[1]

T = int(input())
for t in range(1, T+1):
    metals = int(input())
    relations = [list(map(int, input().split())) for _ in range(metals)]
    treasury = list(map(int, input().split()))
    print("Case #{}: {}".format(t, max_lead(metals, relations, treasury)))