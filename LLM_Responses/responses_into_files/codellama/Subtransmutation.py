read T
for i in range(T):
    N, A, B = map(int, input().split())
    U = list(map(int, input().split()))
    if any(U[i] <= A for i in range(N)) or any(U[i] <= B for i in range(N)):
        print("IMPOSSIBLE")
        continue
    smallest_metal = 1
    while True:
        if all(U[i] >= A + B for i in range(N)):
            break
        for i in range(N):
            if U[i] == 0:
                continue
            elif U[i] - A > 0 and U[i] - B > 0:
                smallest_metal = min(smallest_metal, i)
                break
    print("Case #" + str(i+1) + ": " + str(smallest_metal))