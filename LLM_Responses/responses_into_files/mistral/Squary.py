import sys
from math import sqrt

def squarify(N, K, E):
    total = sum(E)
    squares_sum = sum([i**2 for i in E])
    if total**2 == squares_sum:
        return "IMPOSSIBLE" if K > 1 else []
    else:
        extra = sqrt((squares_sum - total**2) / (2 * K))
        return ["{:.18e}".format(extra)] * (K + 1) if abs(extra) <= 10 ** 18 else "IMPOSSIBLE"

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    E = list(map(int, sys.stdin.readline().split()))
    print("Case #{}: {}".format(_ + 1, ",".join(squarify(N, K, E))))


This code takes input from standard input and outputs the solution for each test case to standard output. The `squarify()` function checks whether a given list is squary or not, and if it's not, it calculates the amount of extra elements needed to make the list squary and returns them as a list. If there is no way to accomplish this, it returns "IMPOSSIBLE". The time complexity of this solution is O(N + K) for each test case, where N is the number of initial elements and K is the maximum number of additional elements that can be added.