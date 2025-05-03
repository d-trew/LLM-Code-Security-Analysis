import sys

T = int(input())
for i in range(1, T + 1):
    R, S = map(int, input().split())
    if R * S <= 14:
        n_ops = min((R - 1) // 2) + (S - 1)
        print("Case #{}: {}".format(i, n_ops))
        for j in range(n_ops):
            a = max(j * 2 + 1, R % 2) if j < S else R - 2 * (R // 2)
            b = min((R - a), j + 1)
            print("{} {}".format(a, b))
    elif T <= 100 and R <= 40 and S <= 40:
        n_ops = min((R - 1) // 2 * (S + 1) + (S - 1))
        print("Case #{}: {}".format(i, n_ops))
        for j in range(n_ops):
            a = max(j * 2 + 1, R % 2) if j < S else R - 2 * (R // 2)
            b = min((R - a), j + 1)
            print("{} {}".format(a, b))
    else:
        sys.exit()