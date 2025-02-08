def reversort_cost(L):
    cost = 0
    for i in range(len(L) - 1):
        j = L.index(min(L[i:]))
        L[i:j+1] = L[i:j+1][::-1]
        cost += (j - i + 1)
    return cost

T = int(input())
for x in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))
    y = reversort_cost(L)
    print(f"Case #{x}: {y}")