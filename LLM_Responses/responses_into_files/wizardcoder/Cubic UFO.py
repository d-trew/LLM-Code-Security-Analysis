import math

def get_shadow(A):
    if A >= 1.00000 and A <= 1.414213:
        return (0, 0), (0, -0.5), (-0.5, 0)
    elif A >= 1.414213 and A <= 1.732050:
        a = math.sqrt(A/2)/2
        return (0, 0), (a, -a), (a, a)
    else:
        raise ValueError("Invalid area")
    
T = int(input())
for i in range(1, T+1):
    A = float(input())
    print("Case #{}:".format(i))
    for point in get_shadow(A):
        print(*point)