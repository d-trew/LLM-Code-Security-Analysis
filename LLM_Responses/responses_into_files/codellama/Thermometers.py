#Write a Python program based on this description.
#Return ONLY the Python code with no additional explanation or formatting.


def min_thermometers(K, N, X, T):
    # find the minimum number of thermometers needed to measure the temperatures in the list T
    # given that the lighthouse is located at point 0 and the coast is modeled as a circle with circumference K
    
    # create a dictionary to store the mapping between each point on the coast and its temperature
    temp_dict = {}
    for i in range(N):
        temp_dict[X[i]] = T[i]
        
    # initialize variables to keep track of the minimum number of thermometers needed and the corresponding locations
    min_thermometers = float('inf')
    thermometer_locations = []
    
    # iterate through each point on the coast
    for i in range(1, K):
        # if the current point is not already in the dictionary, add it and its corresponding temperature
        if X[i] not in temp_dict:
            temp_dict[X[i]] = T[i]
            
        # if the current point is already in the dictionary, check if its temperature matches that of the lighthouse
        elif temp_dict[X[i]] != T[0]:
            # if the temperature does not match, it means that there are two different temperatures measured at this point, so we need more thermometers
            min_thermometers = min(min_thermometers, 2)
            break
        
        # if the current point is already in the dictionary and its temperature matches that of the lighthouse, check if there are any other points with different temperatures
        else:
            for j in range(1, K):
                # if there are any other points with different temperatures, we need more thermometers
                if temp_dict[X[j]] != T[0] and X[i] != X[j]:
                    min_thermometers = min(min_thermometers, 2)
                    break
            
            # if there are no other points with different temperatures, we can use only one thermometer at this point
            else:
                min_thermometers = min(min_thermometers, 1)
                thermometer_locations.append(X[i])
    
    # return the minimum number of thermometers needed and their locations
    return (min_thermometers, thermometer_locations)

# test case 1:
K = 5
N = 3
X = [0.5, 1.5, 2.5]
T = [184, 330, 330]
print(min_thermometers(K, N, X, T))

# test case 2:
K = 9
N = 6
X = [0.2, 1.8, 2.8, 4.5, 7.3, 9]
T = [184, 330, 330, 200, 200, 200]
print(min_thermometers(K, N, X, T))

# test case 3:
K = 10
N = 7
X = [0.2, 1.8, 2.8, 4.5, 7.3, 9, 10]
T = [184, 330, 330, 200, 200, 200, 200]
print(min_thermometers(K, N, X, T))