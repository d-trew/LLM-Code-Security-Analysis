T = int(input())
for _ in range(T):
    R, B, C = map(int, input().split())
    M = list(map(int, input() for _ in range(C)))
    S = list(map(int, input() for _ in range(C)))
    P = list(map(int, input() for _ in range(C)))
    robots = [0] * R
    for i in range(B):
        min_time = float('inf')
        best_cashier = -1
        for j in range(C):
            time = M[j] * (robots.count(j) + 1) + S[j]
            if time < min_time:
                min_time = time
                best_cashier = j
        robots[best_cashier] += 1
    print(f"Case #{_+1}: {min_time}")