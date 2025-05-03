T = int(input())
for t in range(1, T+1):
    N = int(input())
    max_len = 0
    for i in range(N):
        D = list(map(int, input().split()))
        D.sort()
        for j in range(len(D)-4):
            if D[j+4] - D[j] == 5:
                max_len = max(max_len, j+5)
                break
    print("Case #{}: {}".format(t, max_len))