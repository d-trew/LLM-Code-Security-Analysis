from math import factorial

def num_orders(N, V):
    num_visible = 0
    for i in range(len(V)):
        if V[i] == i+1:
            num_visible += 1
    return factorial(N) // (factorial(num_visible) * factorial(N - num_visible)) % (10**9 + 7)

T = int(input())
for case in range(1, T+1):
    N = int(input())
    V = list(map(int, input().split()))
    print("Case #" + str(case) + ": " + str(num_orders(N, V)))