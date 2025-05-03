t = int(input())
for i in range(t):
    n = int(input())
    senators = list(map(int, input().split()))
    plan = []
    while sum(senators) > 0:
        min_majority = float('inf')
        for j in range(n):
            majority = senators[j] // (j + 1)
            if majority < min_majority and all(majority <= senators[k] // (k + 1) for k in range(j)):
                min_majority = majority
                best_party = j
        plan.append(chr(65 + best_party).upper() * min_majority)
        senators = [senators[i] - min_majority for i in range(n)]
    print(f"Case #{i+1}: {' '.join(plan)}")