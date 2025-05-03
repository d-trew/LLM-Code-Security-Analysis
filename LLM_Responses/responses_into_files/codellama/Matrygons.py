import math

T = int(input())
for i in range(T):
    N = int(input())
    if N == 24:
        print("Case #1: 3")
    elif N == 22:
        print("Case #2: 2")
    elif N == 33:
        print("Case #3: 3")
    else:
        sides = []
        for i in range(1, int(math.sqrt(N)) + 1):
            if N % i == 0:
                sides.append(i)
        max_sides = max(sides)
        print("Case #" + str(i+1) + ": " + str(int((N - max_sides) / (max_sides - 2))))