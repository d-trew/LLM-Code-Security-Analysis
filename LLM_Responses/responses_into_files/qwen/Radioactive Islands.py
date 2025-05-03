import math

def min_radiation(A, B, C):
    X = abs(B - A)
    Y = 0
    for c in C:
        D = abs(c - A) if c < A else abs(c - B)
        Y += (D ** 2) / (X + D)
    return Y

T = int(input())
for t in range(1, T+1):
    N, A, B = map(float, input().split())
    C = [float(x) for x in input().split()]
    print(f"Case #{t}: {min_radiation(A, B, C)}")