def solve():
    N, P = map(int, input().split())
    customers = []
    for _ in range(N):
        customers.append(list(map(int, input().split())))

    import itertools
    min_presses = float('inf')

    for customer_orderings in itertools.product(*[itertools.permutations(customer) for customer in customers]):
        
        current_pressure = 0
        total_presses = 0
        
        for customer_ordering in customer_orderings:
            for product_pressure in customer_ordering:
                presses = abs(product_pressure - current_pressure)
                total_presses += presses
                current_pressure = product_pressure
        min_presses = min(min_presses, total_presses)

    return min_presses

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")