R = int(input())
for i in range(R):
    C, F, S = map(int, input().split())
    current_state = []
    for j in range(C):
        current_state.append(list(input()))
    desired_state = []
    for j in range(C):
        desired_state.append(list(input()))
    cost = 0
    while True:
        changed = False
        for i in range(R):
            for j in range(C):
                if current_state[i][j] != desired_state[i][j]:
                    if (current_state[i][j] == "M" and desired_state[i][j] == "G") or (current_state[i][j] == "G" and desired_state[i][j] == "M"):
                        current_state[i][j], cost += F
                    else:
                        if i > 0 and j > 0 and current_state[i - 1][j - 1] == desired_state[i - 1][j - 1]:
                            current_state[i - 1][j - 1], cost += S
                        elif i < R - 1 and j > 0 and current_state[i + 1][j - 1] == desired_state[i + 1][j - 1]:
                            current_state[i + 1][j - 1], cost += S
                        elif i > 0 and j < C - 1 and current_state[i - 1][j + 1] == desired_state[i - 1][j + 1]:
                            current_state[i - 1][j + 1], cost += S
                        elif i < R - 1 and j < C - 1 and current_state[i + 1][j + 1] == desired_state[i + 1][j + 1]:
                            current_state[i + 1][j + 1], cost += S
        if not changed:
            break
print("Case #" + str(i + 1) + ": " + str(cost))