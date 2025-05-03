def min_button_presses(N, P, pressures):
    current_pressure = 0
    total_pressures = 0
    
    for pressure_list in pressures:
        pressure_list.sort()
        for i in range(len(pressure_list)):
            if pressure_list[i] > current_pressure:
                total_pressures += (pressure_list[i] - current_pressure)
                current_pressure = pressure_list[i]
            elif pressure_list[i] < current_pressure:
                total_pressures += (current_pressure - pressure_list[i])
                current_pressure = pressure_list[i]
    
    return total_pressures

T = int(input())
results = []

for case in range(1, T + 1):
    N, P = map(int, input().split())
    pressures = [list(map(int, input().split())) for _ in range(N)]
    result = min_button_presses(N, P, pressures)
    results.append(f"Case #{case}: {result}")

for result in results:
    print(result)