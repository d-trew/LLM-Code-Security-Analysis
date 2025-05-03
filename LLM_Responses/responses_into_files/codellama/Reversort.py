T = int(input())
for t in range(T):
    N = int(input())
    L = [int(x) for x in input().split()]
    cost = 0
    for i in range(N-1):
        j = L.index(min(L[i:])) + i
        cost += j - i + 1
        L[i:j+1] = L[i:j+1][::-1]
    print("Case #" + str(t+1) + ": " + str(cost))