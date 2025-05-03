import sys
from math import inf
import collections
input = sys.stdin.readline

def radiation_dose(A, B, C, N):
    def di(t, i):
        return abs(A - t) + abs(C[i] - t) if i != 0 else abs(A - t)

    def integral(func, a, b, n):
        total = 0
        for i in range(n):
            total += func((i+1)/n * (b-a) + a) - func(a + i/(n*(b-a))*(b-a))
        return total * (b-a)

    def f(t):
        return integral(lambda x: di(x, 0), 0, t, N) + integral(lambda x: di(x, i) - 2 for i in range(1, N+1))

    start = min(A, B)
    end = max(A, B)
    ans = inf
    for i in range(start, end+1):
        if f(i) < ans:
            ans = f(i)
    return ans

T = int(input())
for _ in range(T):
    N, A, B = map(float, input().split())
    C = list(map(float, input().split()))
    print(f"Case #{_+1}: {radiation_dose(A, B, C, N):.3f}")


This Python program reads the number of test cases `T`, followed by the details of each test case: the number of islands `N`, the coordinates of the starting point (A) and destination (B), and the y-coordinates of the islands (Ci). It then calculates the optimal radiation dose for each test case using the function `radiation_dose(A, B, C, N)`. The function uses the definite integral to calculate the radiation received from the general environment and each island along the path. Finally, it prints the minimum radiation dose for each test case.