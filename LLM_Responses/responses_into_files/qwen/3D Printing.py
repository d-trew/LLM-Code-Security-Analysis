T = int(input())
for _ in range(T):
    C1, M1, Y1, K1 = map(int, input().split())
    C2, M2, Y2, K2 = map(int, input().split())
    C3, M3, Y3, K3 = map(int, input().split())
    for c in range(C1+1):
        for m in range(M1+1):
            for y in range(Y1+1):
                for k in range(K1+1):
                    if c + m + y + k == 10**6 and min(c, m, y, k) <= min(C1, M1, Y1, K1) and \
                       min(c, m, y, k) <= min(C2, M2, Y2, K2) and min(c, m, y, k) <= min(C3, M3, Y3, K3):
                        print(f"Case #{_+1}: {c} {m} {y} {k}")
                        break
                else:
                    continue
                break
            else:
                continue
        else:
            continue
    else:
        print("IMPOSSIBLE")