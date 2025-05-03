import math
def solve(N, P):
    target_pressures = []
    for i in range(N):
        target_pressures.append([])
        for j in range(P):
            target_pressures[i].append(int(input()))
    min_button_presses = 0
    for i in range(N):
        current_target = 0
        for j in range(P):
            if current_target < target_pressures[i][j]:
                min_button_presses += abs(current_target - target_pressures[i][j])
                current_target = target_pressures[i][j]
    return min_button_presses