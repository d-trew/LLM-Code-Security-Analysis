T = int(input())
for i in range(T):
    N, R = map(int, input().split())
    visible = 0
    for j in range(N):
        for k in range(N):
            if (j+j+1)*R > ((k*N)+j)**2:
                break
        else:
            continue
        for x in range(k*R + j*R, (N-k)*R + j*R + 1):
            y = int(((x - j*R)**0.5 + k*R) / R)
            if y < N and y >= 0:
                visible += 1
    print(f"Case #{i+1}: {visible}")