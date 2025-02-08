def solve():
    N = int(input())
    D = list(map(int, input().split()))

    max_paid = 0
    
    def count_paid(order):
        paid_count = 0
        last_paid = -1
        for i in range(len(order)):
            if i == 0 or order[i] >= last_paid:
                paid_count += 1
                last_paid = order[i]
        return paid_count

    import itertools
    for order_tuple in itertools.permutations(D):
        order = list(order_tuple)
        max_paid = max(max_paid, count_paid(order))

    return max_paid

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")