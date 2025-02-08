def solve():
    N = int(input())
    dice = []
    for _ in range(N):
        dice.append(list(map(int, input().split())))

    max_len = 0

    for i in range(1 << (N * 6)):
        current_dice = []
        for j in range(N):
            die_index = (i >> (j * 6)) & 63
            if die_index < 6:
                current_dice.append(dice[j][die_index])

        if not current_dice:
            continue

        current_dice.sort()
        
        current_len = 1
        for k in range(1, len(current_dice)):
            if current_dice[k] == current_dice[k-1] + 1:
                current_len += 1
            else:
                max_len = max(max_len, current_len)
                current_len = 1
        max_len = max(max_len, current_len)

    return max_len

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")