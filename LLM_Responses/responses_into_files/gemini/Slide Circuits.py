def solve():
    B, S, N = map(int, input().split())
    slides = []
    for _ in range(S):
        slides.append(list(map(int, input().split())))
    
    enabled_slides = set()
    results = []

    for _ in range(N):
        op, l, r, m = input().split()
        l, r, m = int(l), int(r), int(m)
        
        affected_slides = set()
        for i in range(l, r + 1):
            if i % m == 0:
                affected_slides.add(i -1)

        if op == 'E':
            enabled_slides.update(affected_slides)
        else:
            enabled_slides.difference_update(affected_slides)

        found_solution = False
        for i in range(S):
            if i not in enabled_slides:
                temp_enabled = set(enabled_slides)
                temp_enabled.add(i)
                
                adj = [[] for _ in range(B + 1)]
                in_degree = [0] * (B + 1)
                out_degree = [0] * (B + 1)
                
                for j in temp_enabled:
                    u, v = slides[j]
                    adj[u].append(v)
                    out_degree[u] += 1
                    in_degree[v] += 1

                
                is_fun = True
                
                
                
                if is_fun:
                    results.append(i + 1)
                    found_solution = True
                    break
        if not found_solution:
            results.append('X')

    return " ".join(map(str, results))

T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}: {solve()}")