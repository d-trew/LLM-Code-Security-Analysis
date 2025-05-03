T = int(input())
for _ in range(T):
    N = int(input())
    mistakes_A = 0
    mistakes_B = 0
    A_wins = [False] * (N + 1)
    for i in range(1, N + 1):
        if i % 2 == 1:
            A_wins[i] = True
        else:
            B_wins = False
            for j in range(1, min(i, N) + 1):
                if (A_wins[j - 1] and i != j) or ((i - j) % 2 == 0):
                    A_wins[i] = True
                    mistakes_B += 1
                    break
                elif i - j == 1:
                    B_wins = True
            if not B_wins:
                for j in range(i + 1, N + 1):
                    if (A_wins[j - 1] and j != i) or ((j - i) % 2 == 0):
                        A_wins[i] = False
                        mistakes_A += 1
                        break
    print(f"Case #{_ + 1}: {mistakes_A} {mistakes_B}")