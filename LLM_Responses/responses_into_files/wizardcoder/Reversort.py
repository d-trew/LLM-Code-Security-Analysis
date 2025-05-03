import sys

T = int(input())
for i in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    total_cost = 0
    for j in range(N-1, 0, -1):
        index = L.index(min(L[j:]) + j)
        L = L[:index+1][::-1] + L[index+1:]
        total_cost += (index+1)
    print("Case #{}: {}".format(i, total_cost))