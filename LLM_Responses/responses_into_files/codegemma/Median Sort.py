def sort(n: int) -> list[int]:        # Function for sorting N elements based on median questions  


     elements = [i +1for i in range ( n)]   ## Initialize the array of numbers to be sorted

      median=[]                          ### Array that will store medians 
       done=False                        #### Boolean variable used as a flag when we have found all needed information about elements order. It is set True only after Q questions are asked


        while not done:  # Loop until answer for the last question has been received and processed

            if len(median) == n - 1 : # If medians of N-2 pairs were already determined, we can sort remaining two in comparison with each other.
                done = True          ## Set flag to true as all necessary information is gathered


             else:  # Otherwise get the median for another pair and add it into array

                 i , j=random .randint(0,(n-1)), random