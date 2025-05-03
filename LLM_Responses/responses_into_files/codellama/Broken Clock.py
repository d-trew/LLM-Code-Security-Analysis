import math

def time_from_angles(A, B, C):
    # Convert angles from degrees to radians
    A *= math.pi / 180
    B *= math.pi / 180
    C *= math.pi / 180
    
    # Calculate the time in seconds and nanoseconds
    s = int(A) * 3600 + int(B) * 60 + int(C)
    ns = (int(A) * 3600 + int(B) * 60 + int(C)) % 10 ** 9
    
    # Return the time in hours, minutes, seconds and nanoseconds
    return s // 3600, (s % 3600) // 60, (s % 60), ns

def main():
    # Test case 1: All hands point up
    A = 0
    B = 0
    C = 0
    print(f"Case #{1}: {time_from_angles(A, B, C)}")
    
    # Test case 2: Hours hand at 6 hours and minutes hand at 30 minutes
    A = 6
    B = 30
    C = 0
    print(f"Case #{2}: {time_from_angles(A, B, C)}")
    
    # Test case 3: Hours hand at 1 hour and minutes hand at 45 minutes
    A = 1
    B = 45
    C = 0
    print(f"Case #{3}: {time_from_angles(A, B, C)}")
    
if __name__ == "__main__":
    main()