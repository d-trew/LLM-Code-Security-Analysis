# Python code here     


def findPath(N, P):        ## Function definition for finding path without conflict with Lydia's moves   



            path = []      ### Initialize an empty list called 'paths'. It will store the valid paths.  

             for i in range (2* N - 3) :          # Iterate over each character of string
                 if P[i] == "E" and path[-1:] != ["S"]:   ## Check if current move is east, but last step isn't south    


                     path.append("N")  ### Append north to the list as it doesn’ t conflict with Lydia moves 



                elif (P [ i ]== ' S'):
                    if path[-1:] != ["E"]:   ## Check if current move is South, but last step isn't east    


                        path.append("N")  ### Append north to the list as it doesn’ t conflict with Lydia moves 



                else:

                     pass        # If both conditions are not met then no need for any action just continue iterating through string P   
                 if i == N -1 :      ## Check if we have reached half of our path, now start moving south  


                    path.append("S")    ### Append South to the list as it doesn’t conflict with Lydia moves 



                elif (i >=N and len(Path) <=2*n-3):   # If current move is not north then append east or continue iterating if we have already reached half of path  

                    path.append("E")    ### Append East to the list as it doesn’t conflict with Lydia moves 



                else:
                     pass        ## No need for any action just keep moving forward in south direction until end is achieved   


            return ''.join(Path)      # Convert our path from a lisr of characters into string and return  

    T = int (input())       ### Read the number test cases T 



     for i case range :        ## Iterate over each Test Case
         N=int()              #### Input N for current maze size   


          P=( input().strip)      #Input P from user as a string of characters  

           print("Case #{}: {}".format(i+1, findPath (n , p)))    ### Print the result with case number and path