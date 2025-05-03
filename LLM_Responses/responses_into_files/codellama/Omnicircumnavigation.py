import math

def is_omnicircumnavigation(points):
    # Calculate the distance between each pair of successive points
    distances = [(math.sqrt((points[i+1][0]-points[i][0])**2 + (points[i+1][1]-points[i][1])**2 + (points[i+1][2]-points[i][2])**2), i) for i in range(len(points)-1)]
    
    # Sort the distances in ascending order
    sorted_distances = sorted(distances, key=lambda x: x[0])
    
    # Initialize a variable to keep track of the total distance traveled
    total_distance = 0
    
    # Iterate through the sorted distances
    for i in range(len(sorted_distances)):
        # Add the current distance to the total distance
        total_distance += sorted_distances[i][0]
        
        # Check if the total distance is greater than 4 times the radius of the sphere
        if total_distance > 4:
            return False
    
    # If the total distance is less than or equal to 4 times the radius of the sphere, then the path is an omnicircumnavigation
    return True

# Test case 1:
print("Case #1:", end=" ")
points = [(0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5)]
if is_omnicircumnavigation(points):
    print("YES")
else:
    print("NO")

# Test case 2:
print("Case #2:", end=" ")
points = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1), (-1, 1, 1), (-1, 1, 0), (-1, 0, 0)]
if is_omnicircumnavigation(points):
    print("YES")
else:
    print("NO")

# Test case 3:
print("Case #3:", end=" ")
points = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 1, -1), (1, 0, -1), (-1, 0, -1), (-1, -1, -1), (-1, -1, 0), (-1, -1, 1)]
if is_omnicircumnavigation(points):
    print("YES")
else:
    print("NO")

# Test case 4:
print("Case #4:", end=" ")
points = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 1, -1), (1, 0, -1), (-1, 0, -1), (-1, -1, -1), (-1, -1, 0), (-1, -1, 1), (1, 0, 0)]
if is_omnicircumnavigation(points):
    print("YES")
else:
    print("NO")