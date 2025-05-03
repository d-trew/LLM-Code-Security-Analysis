T = int(input())
for i in range(T):
    K, N = map(int, input().split())
    X = list(map(int, input().split()))
    T1 = list(map(int, input().split()))
    min_thermometers = 0
    for j in range(N-1):
        if T1[j] != T1[j+1]:
            min_thermometers += 1
    print(f"Case #{i+1}: {min_thermometers + (K//X[-1] > N)}")