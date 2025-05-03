def solve_molecules(n, codium, jamarium):
    min_codium = min([c for c, j in zip(codium, jamarium) if c < j] + [0])
    max_jamarium = max([j for c, j in zip(codium, jamarium) if c > j] + [10**9+1])
    
    while min_codium + 1 < max_jamarium:
        mid = (min_codium + max_jamarium) // 2
        
        possible = True
        prev_weight = 0
        for c, j in zip(codium, jamarium):
            if c > mid or j > mid*2 - c:
                possible = False
                break
            prev_weight = max(prev_weight, c + j)
        
        if not possible or prev_weight != codium[-1] + jamarium[-1]:
            min_codium = mid
        else:
            max_jamarium = mid
    
    return (min_codium, max_jamarium - 1) if min_codium + 1 < max_jamarium else "IMPOSSIBLE"

t = int(input().strip())
for i in range(1, t+1):
    n = int(input().strip())
    codium = [int(x) for x in input().strip().split()]
    jamarium = [int(x) for x in input().strip().split()]
    
    result = solve_molecules(n, codium, jamarium)
    print("Case #{}: {}".format(i, result))