import math

def solve(N, W, H, P, Q, R, S, A_list, B_list):
    # Calculate the area of each patch
    areas = []
    for i in range(N):
        x1, y1, x2, y2 = A_list[i], B_list[i], C_list[i], D_list[i]
        areas.append((x2-x1)*(y2-y1))
    
    # Calculate the total area of the cake
    total_area = W*H
    
    # Initialize variables to store the minimum difference between your and your twin's enjoyment
    min_diff = math.inf
    optimal_x = None
    
    # Iterate through each possible cut point x
    for x in range(total_area+1):
        left_area = total_area - x
        
        # Calculate the sum of the enjoyment you and your twin will receive from each patch
        your_enjoyment = 0
        twins_enjoyment = 0
        for i in range(N):
            if areas[i] > left_area:
                # If the area of the patch is greater than the remaining area, you will eat all of it and your twin will eat nothing
                your_enjoyment += A_list[i] * (left_area / areas[i])
            else:
                # Otherwise, both you and your twin will eat part of the patch
                your_enjoyment += A_list[i]
                twins_enjoyment += B_list[i] * (left_area / areas[i])
        
        # Calculate the absolute difference between your and your twin's enjoyment
        diff = abs(your_enjoyment - twins_enjoyment)
        
        # Update the minimum difference and optimal cut point if necessary
        if diff < min_diff:
            min_diff = diff
            optimal_x = x
    
    return "Case #1: {}/{}".format(min_diff, total_area - optimal_x)