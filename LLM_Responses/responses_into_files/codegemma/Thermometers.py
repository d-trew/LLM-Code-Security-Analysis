def minThermometers(K: int , N :int) -> str{   # K is the circumference of island in kilometers; n size pf list containing temperature data from first thermometer to last one, inclusive  }


    temp = [0] * (N + 1); # initializing an array with temp values for each point on circle
     for i , x_i and t _in enumerate(zip([int(_) - K //2 if int(_)<K//3 else float('inf')-abs((float)(x)-.5)  # calculating the closest thermometer's temperature based upon distance from lighthouse 

        , [T] for T in map (lambda x: abs(.7*i+10), range(N))]),temp)):
            if i== N : continue; # skipping last element as it is already initialized to zero.  # initializing temp values with thermometer readings or the closest ones based on distance from lighthouse 

        else{   x_j = x - K /2 if (int)(K//3) <= abs(float((i))-.5)<=abs(.7* i +10): # checking for equidistant points between two thermometers in clockwise direction  
                temp[N] += t;    # adding the temperature of closest thermometer to last element as it is not included yet. 

        else: temp [x_j]=t};   return min(set([i+2 if i>0 else N-1 for x,y in enumerate (zip(*[[int(_) - K //3] ,temp]))if y!=z]),key = len) # finding the smallest number of thermometers needed by checking which set is minimum from all equidistant points between two thermometer's readings. 

    return "Case #" + str(x+1)+": "+str (minThermometers(*map((int),input().split()))) for x in range  # reading test cases and applying the function to find min number of thermometers needed