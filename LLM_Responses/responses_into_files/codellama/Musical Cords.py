import math
def longest_cords(N, R, K):
    # Initialize a list to store the lengths of all possible cords
    cord_lengths = []
    
    # Calculate the length of each possible cord
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the distance between the two attachment points
            distance = math.sqrt((R*math.cos(i*360/N))**2 + (R*math.sin(i*360/N))**2) - math.sqrt((R*math.cos(j*360/N))**2 + (R*math.sin(j*360/N))**2)
            cord_lengths.append(distance)
    
    # Sort the list of lengths in non-increasing order
    cord_lengths.sort(reverse=True)
    
    # Return the K longest cords
    return cord_lengths[:K]