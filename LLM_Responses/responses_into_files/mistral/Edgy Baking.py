import math
from itertools import accumulate

def solve(N, P):
    total_perim = sum([2 * (w + h) for w, h in zip(*[[int(x) for x in input().split()] for _ in range(N)])])
    if total_perim > P:
        return float('inf')

    max_perim = P - total_perim
    perim_diff = [0] * N
    for i, (w, h) in enumerate(zip(*[[int(x) for x in input().split()] for _ in range(N))):
        perim = 2 * (w + h)
        if max_perim > 0:
            half_perim = math.sqrt((max_perim / 2) ** 2 - ((w - h) ** 2))
            if half_perim <= min(w, h):
                perim_diff[i] += half_perim * 2
                max_perim -= half_perim * 2

    return sum(accumulate(perim_diff))

T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    print(f"Case #{_+1}: {solve(N, P):.6f}")


This code takes the number of test cases and iterates through each one, calculating the initial total perimeter sum of the cookies. If it exceeds the desired perimeter, it returns infinity. Otherwise, it calculates the maximum possible perimeter difference for each cookie that can be cut without going over the maximum perimeter difference. Finally, it calculates the new perimeter sum and prints the result with 6 decimal places.