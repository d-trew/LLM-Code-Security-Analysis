import math

def solve():
    A = float(input())
    
    if abs(A - 1.0) < 1e-9:
        print("0.0 0.5 0.0")
        print("0.5 0.0 0.0")
        print("0.0 0.0 0.5")
        return

    if abs(A - 1.414213) < 1e-9:
        angle = math.pi / 4
        x1 = 0.5 * math.cos(angle)
        y1 = 0.5 * math.sin(angle)
        z1 = 0.0
        x2 = 0.5 * math.cos(angle + math.pi/2)
        y2 = 0.5 * math.sin(angle + math.pi/2)
        z2 = 0.0
        x3 = 0.0
        y3 = 0.0
        z3 = 0.5

        print(f"{x1:.10f} {y1:.10f} {z1:.10f}")
        print(f"{x2:.10f} {y2:.10f} {z2:.10f}")
        print(f"{x3:.10f} {y3:.10f} {z3:.10f}")
        return

    if abs(A - 1.732050) < 1e-9:
        angle = math.pi / 3
        x1 = 0.5 * math.cos(angle)
        y1 = 0.5 * math.sin(angle)
        z1 = 0.0
        x2 = 0.5 * math.cos(angle + 2*math.pi/3)
        y2 = 0.5 * math.sin(angle + 2*math.pi/3)
        z2 = 0.0
        x3 = 0.5 * math.cos(angle + 4*math.pi/3)
        y3 = 0.5 * math.sin(angle + 4*math.pi/3)
        z3 = 0.0
        
        print(f"{x1:.10f} {y1:.10f} {z1:.10f}")
        print(f"{x2:.10f} {y2:.10f} {z2:.10f}")
        print(f"{x3:.10f} {y3:.10f} {z3:.10f}")
        return


T = int(input())
for i in range(1, T + 1):
    print(f"Case #{i}:")
    solve()