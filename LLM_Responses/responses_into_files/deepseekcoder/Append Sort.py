def solve():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        X = list(map(int, input().split()))
        ops = 0
        for i in range(N - 1):
            if X[i] >= X[i+1]:
                diff = X[i] - X[i+1] + 1
                X[i+1] += diff
                ops += diff
        print("Case #{}: {}".format(tc, ops))

solve()