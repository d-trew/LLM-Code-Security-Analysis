import math

def solve(A):
    # Calculate the diagonal of the cube which will be its side length in the plane
    d = math.sqrt(2) * A / (1 + math.sin(math.pi/4)) 
    
    # The centers of any three non-pairwise-opposing faces are at these coordinates
    x1, y1, z1 = 0.5*d, -3, 0.5*d
    x2, y2, z2 = -0.5*d, -3, -0.5*d
    x3, y3, z3 = 0.5*d, -3, -0.5*d
    
    return (x1, y1, z1), (x2, y2, z2), (x3, y3, z3)

T = int(input())
for i in range(1, T+1):
    A = float(input())
    centers = solve(A)
    
    print('Case #{}:'.format(i))
    for center in centers:
        print('{:.7f} {:.7f} {:.7f}'.format(*center))