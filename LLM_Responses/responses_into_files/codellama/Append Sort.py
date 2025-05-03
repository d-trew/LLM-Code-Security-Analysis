T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    x = [str(i) for i in X]
    res = 0
    for i in range(1, N):
        while len(x[i-1]) < len(x[i]):
            if not str(int(x[i][:-1]) + 1).endswith('9'):
                break
            res += 1
    print(f"Case #{_+1}: {res}")