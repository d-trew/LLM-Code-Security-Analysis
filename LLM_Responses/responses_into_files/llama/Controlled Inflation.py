T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    pressures = [list(map(int, input().split())) for _ in range(N)]
    prev_target = 0
    button_presses = 0
    for customer in pressures:
        for product_pressure in customer:
            if product_pressure != prev_target:
                if product_pressure > prev_target:
                    button_presses += product_pressure - prev_target
                else:
                    button_presses -= prev_target - product_pressure
            prev_target = product_pressure
    print(f"Case # {_ + 1}: {button_presses}")