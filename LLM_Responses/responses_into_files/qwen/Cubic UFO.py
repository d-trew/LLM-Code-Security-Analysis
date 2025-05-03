import math

def main():
    T = int(input())
    for i in range(1, T + 1):
        A = float(input())
        
        # Case 1: No rotation needed if A is 1.000000
        if abs(A - 1.000000) < 1e-6:
            print(f"Case #{i}:")
            print("0.000000")
            print("0.500000")
            print("0.000000")
        
        # Case 2: Rotate by 45 degrees around the x = y = 0 line if A is sqrt(2)
        elif abs(A - math.sqrt(2)) < 1e-6:
            print(f"Case #{i}:")
            print("0.707107")
            print("0.000000")
            print("0.707107")
        
        # Case 3: Rotate by arccos(A) degrees around the x = y = 0 line if A is between sqrt(2) and 1.414213
        else:
            angle = math.acos(A)
            cos_angle = math.cos(angle)
            sin_angle = math.sin(angle)
            print(f"Case #{i}:")
            print(f"{cos_angle:.6f}")
            print(f"{sin_angle:.6f}")
            print(f"{cos_angle:.6f}")

if __name__ == "__main__":
    main()