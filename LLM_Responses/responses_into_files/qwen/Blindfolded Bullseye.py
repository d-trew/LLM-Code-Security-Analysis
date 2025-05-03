import sys

input = sys.stdin.read
data = input().split()

T = int(data[0])
A = int(data[1])
B = int(data[2])

index = 3

for _ in range(T):
    R = (A + B) // 2
    X, Y = 0, 0
    
    for _ in range(300):
        print(X, Y)
        sys.stdout.flush()
        
        response = input().strip()
        if response == "CENTER":
            break
        elif response != "HIT" and response != "MISS":
            print("WRONG")
            sys.exit(1)
    
    # Adjust the radius based on the response
    if response == "HIT":
        R -= 1
    else:
        R += 1
    
    # Adjust the center based on the response
    if response == "HIT" and X != 0:
        if Y != 0:
            X, Y = -X, -Y
        else:
            X *= -1
    elif response == "MISS":
        if X != 0:
            X *= -1
        elif Y != 0:
            Y *= -1
    
    # Ensure the radius is within bounds
    R = max(A, min(B, R))
    
    # Update the center based on the new radius
    X, Y = 0, 0

print("CENTER")