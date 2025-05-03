import math

T = int(input())
for t in range(T):
    N = int(input())
    columns = []
    for i in range(N):
        x, y, h = map(int, input().split())
        columns.append((x, y, h))
    
    # sort the columns by their heights in descending order
    columns.sort(key=lambda col: col[2], reverse=True)
    
    # create a dictionary to store the relationships between the columns
    column_dict = {}
    for i in range(N):
        column_dict[i+1] = [columns[i][0], columns[i][1]]
    
    # initialize the first three columns as the starting points
    col1, col2, col3 = 1, 2, 3
    
    # loop through the remaining columns and find the next column to connect to the previous one
    for i in range(4, N+1):
        # find the closest point on the line segment between col1 and col2 that is not yet connected
        min_dist = math.inf
        closest_point = None
        for j in range(col1, col2+1):
            dist = get_distance((column_dict[j][0], column_dict[j][1]), (column_dict[i][0], column_dict[i][1]))
            if dist < min_dist:
                min_dist = dist
                closest_point = j
        
        # connect the next column to the closest point on the line segment between col1 and col2
        column_dict[i] = [column_dict[closest_point][0], column_dict[closest_point][1]]
        
        # update col1, col2, and col3 to be the next three columns in the sequence
        if i == col1 + 3:
            col1 += 3
            col2 += 3
            col3 += 3
        elif i == col2 + 3:
            col2 += 3
            col3 += 3
        else:
            col3 += 3
    
    # output the possible ordering of the columns
    print("Case #" + str(t+1) + ": " + str(col1) + " " + str(col2) + " " + str(col3))
    
def get_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)