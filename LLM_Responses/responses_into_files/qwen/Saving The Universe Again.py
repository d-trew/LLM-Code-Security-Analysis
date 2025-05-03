def min_hacks(D, P):
    n = len(P)
    damage = P.count('S')
    if damage <= D:
        return 0
    
    max_singles = sum(1 for i in range(n-1) if P[i] == 'C' and P[i+1] == 'S')
    if max_singles * 2 > damage:
        return -1
    
    # Binary search for the minimum number of hacks
    left, right = 0, max_singles
    while left < right:
        mid = (left + right) // 2
        if can_reduce_damage(D, P, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

def can_reduce_damage(D, P, hacks):
    n = len(P)
    damage = P.count('S')
    if damage <= D:
        return True
    
    for _ in range(hacks):
        max_singles = sum(1 for i in range(n-1) if P[i] == 'C' and P[i+1] == 'S')
        if max_singles * 2 > damage:
            return False
        # Simulate swapping adjacent CS pairs
        for i in range(n-1):
            if P[i] == 'C' and P[i+1] == 'S':
                P = P[:i] + 'SC' + P[i+2:]
                break
    
    return damage <= D

# Read input
T = int(input())
results = []

for i in range(1, T+1):
    D, P = input().split()
    D = int(D)
    result = min_hacks(D, P)
    if result == -1:
        results.append(f"Case #{i}: IMPOSSIBLE")
    else:
        results.append(f"Case #{i}: {result}")

# Output results
for result in results:
    print(result)