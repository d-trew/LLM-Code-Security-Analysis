def min_button_presses(customers):
    n = len(customers)
    products = [sorted([i for i in customer]) for customer in customers]
    presses = 0
    current_pressure = 0
    
    for product in products:
        for target_pressure in product:
            if target_pressure > current_pressure:
                presses += target_pressure - current_pressure
                current_pressure = target_pressure
            else:
                presses += current_pressure - target_pressure + 1
                current_pressure = target_pressure + 1
    return presses

T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())
    customers = [list(map(int, input().split())) for _ in range(N)]
    print('Case #{}: {}'.format(t, min_button_presses(customers)))