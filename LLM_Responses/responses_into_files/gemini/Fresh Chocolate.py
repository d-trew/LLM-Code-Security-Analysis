def solve():
    N, P = map(int, input().split())
    groups = list(map(int, input().split()))

    max_fresh = 0
    import itertools
    for perm in itertools.permutations(groups):
        leftover = 0
        fresh_count = 0
        for group_size in perm:
            needed = group_size - leftover
            if needed <= 0:
                leftover -= group_size
            else:
                packs = (needed + P - 1) // P
                leftover = packs * P - needed
                fresh_count += 1
        max_fresh = max(max_fresh, fresh_count)
    return max_fresh

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")