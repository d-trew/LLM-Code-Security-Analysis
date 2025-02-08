def solve():
    N = int(input())
    molecules = []
    for _ in range(N):
        C, J = map(int, input().split())
        molecules.append((C, J))

    best_c = float('inf')
    best_j = float('inf')
    found_solution = False

    for c in range(1, 101):
        for j in range(1, 101):
            weights = []
            for C, J in molecules:
                weights.append(C * c + J * j)
            
            is_sorted = all(weights[i] < weights[i+1] for i in range(len(weights)-1))
            if is_sorted:
                if c < best_c:
                    best_c = c
                    best_j = j
                    found_solution = True
                elif c == best_c and j < best_j:
                    best_j = j
                    found_solution = True

    if found_solution:
        return f"{best_c} {best_j}"
    else:
        return "IMPOSSIBLE"

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")