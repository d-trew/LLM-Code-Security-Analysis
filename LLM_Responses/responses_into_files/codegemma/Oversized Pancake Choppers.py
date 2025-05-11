# Import necessary libraries here


def calculate(N: int , D :int) -> str {        ## Function for calculating minimum cuts needed     



   A = [0] * N  ### Array to store the angles of each slice

      for i in range (1,D):         #### Read angle values into array
          a= input().split() 


    # Sort and sort reversely by size. This is necessary for later cuts as we want smaller pieces first        ##Sort both arrays based on their respective elements  in ascending order of magnitude

   A = sorted(map (int, a))[::-1]     



      total_cuts=0         #### Initialize total cut count to 
    for i in range((N - D)):          ### Iterate over the array until we have enough slices for all diners. Each iteration is one more slice needed and therefore another potential set of cuts

        minangle = A[i]            ## Extract minimum angle from current stack


                # Find two angles which sum up to minAngle
         for j in range(N - D + i): 



             if (A[(j)]+  a [(D-1)-((n) )])== Min_anlge:

                 totalcuts +=2      ## Increment total cut count by one for each pair of angles we combine


    return f'Case # {i}: ' , str(TotalCutCount + N - D))   # Return the case number and minimum cuts required 



if __name__ == "__main__":  
     T = int (input()) ## Read total test cases

      for i in range((1, T+2)):    ## Iterate over each of those tests


          N ,D= map(int,( input().split()))   #Read number pf slices and diners for current case 



        print calculate