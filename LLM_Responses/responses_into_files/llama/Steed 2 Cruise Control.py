T = int(input())
for t in range(1, T+1):
    D, N = map(int, input().split())
    horses = []
    for _ in range(N):
        K, S = map(int, input().split())
        horses.append((K, S))
    max_speed = 0
    for i in range(len(horses)):
        for j in range(i+1, len(horses)):
            if horses[i][1] > horses[j][1]:
                max_speed = max(max_speed, horses[i][1])
            else:
                max_speed = max(max_speed, horses[j][1])
    print(f"Case #{t}: {max_speed:.6f}")