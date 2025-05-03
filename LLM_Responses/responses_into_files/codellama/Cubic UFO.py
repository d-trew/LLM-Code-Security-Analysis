import math

T = int(input())
for i in range(1, T+1):
    A = float(input())
    print("Case #" + str(i) + ":")
    if (A == 1.000000 or A == 1.414213):
        print("0.000000, 0.000000, 0.000000")
        print("0.000000, 0.000000, 0.000000")
        print("0.000000, 0.000000, 0.000000")
    elif (A == 1.732050):
        print("0.000000, -0.866025, 0.000000")
        print("0.000000, 0.000000, 1.000000")
        print("-0.866025, -0.500000, 0.000000")
    else:
        theta = math.acos(A/math.sqrt(2))
        x = math.sin(theta) * math.cos(theta)
        y = math.sin(theta) * math.sin(theta)
        z = math.cos(theta)
        print("0.000000, " + str(x) + ", 0.000000")
        print("0.000000, " + str(y) + ", 1.000000")
        print("-" + str(z) + ", -0.500000, 0.000000")