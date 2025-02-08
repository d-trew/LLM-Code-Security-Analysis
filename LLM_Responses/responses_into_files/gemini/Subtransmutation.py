def solve():
    N, A, B = map(int, input().split())
    U = list(map(int, input().split()))

    def check(start_metal):
        counts = [0] * (N + 1)
        counts[start_metal] = 1
        
        q = [counts.copy()]
        visited = {tuple(counts)}

        while q:
            curr_counts = q.pop(0)
            
            possible = True
            for i in range(1, N + 1):
                if curr_counts[i] < U[i-1]:
                    possible = False
                    break
            if possible:
                return True

            for i in range(1,N+1):
                if curr_counts[i] > 0:
                    next_counts = curr_counts[:]
                    next_counts[i] -= 1
                    
                    if i - A > 0:
                        next_counts[i - A] += 1
                    if i - B > 0:
                        next_counts[i - B] += 1
                    
                    if tuple(next_counts) not in visited:
                        visited.add(tuple(next_counts))
                        q.append(next_counts)
        return False

    for i in range(1, 1001):
        if check(i):
            return i
    return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")