Here is a Python program that can solve this problem by calculating the number of pillars visible from the viewpoint. The code uses basic geometry and does not require any special libraries or packages. It assumes that all pillars have their bases on the floor and ceiling, which is true for the given problem description. 


import math

def visible_pillars(N, R):
    # Calculate the number of pillars in each row/column
    num_pillars = N * N - 1  
    
    # Calculate the distance from the viewpoint to any point on a pillar's boundary
    max_distance = math.sqrt(N ** 2 + (N / 2) ** 2)
    
    # Check if each pillar is visible
    for i in range(num_pillars):
        # Calculate the distance from the viewpoint to the center of the pillar
        x = N * math.cos((i + 1) * (360 / num_pillars))
        y = N * math.sin((i + 1) * (360 / num_pillars))
        
        distance = math.sqrt(x ** 2 + y ** 2)
        
        # If the pillar is not visible, subtract one from the total count
        if distance < max_distance:
            num_pillars -= 1
    
    return num_pillars

# Read the number of test cases
T = int(input())
for i in range(T):
    # Read N and R for each test case
    N, R = map(int, input().split())
    print("Case #{}: {}".format(i + 1, visible_pillars(N, R)))

This program first calculates the total number of pillars in the gallery. It then iteratively checks each pillar to see if it is visible from the viewpoint. The visibility of a pillar is determined by calculating its distance from the center of the viewpoint and comparing it with the maximum possible distance (i.e., the diagonal of the square). If a pillar's distance is less than this maximum distance, it is considered visible and does not contribute to the total count. The program then prints out the number of visible pillars for each test case.