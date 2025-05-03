T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    cost = 0
    for i in range(1, N):
        j = L.index(min(L[i:]))
        L[:j+1] = reversed(L[:j+1])
        cost += j - i + 1
    print(f"Case #{_+1}: {cost}")