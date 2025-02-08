import heapq

def solve():
    N = int(input())
    E = list(map(int, input().split()))
    S = list(map(int, input().split()))
    D = []
    for _ in range(N):
        D.append(list(map(int, input().split())))
    
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))

    results = []
    for u, v in queries:
        u -= 1
        v -= 1
        
        pq = [(0, u, E[u], [])] # (time, current_city, remaining_endurance, path)
        visited = set()

        while pq:
            time, current_city, remaining_endurance, path = heapq.heappop(pq)
            
            if current_city == v:
                results.append(time)
                break

            if (current_city, tuple(path)) in visited:
                continue
            visited.add((current_city, tuple(path)))

            for next_city in range(N):
                if D[current_city][next_city] != -1:
                    distance = D[current_city][next_city]
                    if distance <= remaining_endurance:
                        new_time = time + distance / S[current_city]
                        new_remaining_endurance = remaining_endurance - distance
                        new_path = path + [current_city]
                        heapq.heappush(pq, (new_time, next_city, new_remaining_endurance, new_path))
                        
                    
                    new_time = time + distance / S[next_city]
                    heapq.heappush(pq,(new_time, next_city, E[next_city], path + [current_city]))


    return " ".join(map(str, results))

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")