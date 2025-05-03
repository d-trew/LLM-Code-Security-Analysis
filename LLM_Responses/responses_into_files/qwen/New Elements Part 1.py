t = int(input())
for i in range(1, t+1):
    n = int(input())
    orderings = set()
    for _ in range(n):
        ci, j = map(int, input().split())
        for k in range(min(ci, j)+1):
            ordering = f"({ci-k},{j-k}) ({k},{k})"
            if (ci-k) > (j-k): 
                orderings.add(ordering)
    print(f"Case #{i}: {len(orderings)}")