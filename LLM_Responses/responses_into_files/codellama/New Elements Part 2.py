T = int(input())
for _ in range(T):
    N = int(input())
    c_weights = []
    for _ in range(N):
        Ci, Ji = map(int, input().split())
        c_weights.append(Ci + Ji)
    c_weights.sort()
    for C in range(1, 110):
        for J in range(1, 110):
            if all((C * i) + (J * (N - i)) == c_weights[i] for i in range(N)):
                print(f"Case #{_+1}: {C} {J}")
                break
    else:
        print(f"Case #{_+1}: IMPOSSIBLE")