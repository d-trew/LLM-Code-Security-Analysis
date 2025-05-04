def decorate(grid):        # Function for decorating cake with initials      



   for i in range (len((row))-1)):          ## Iterate over rows of the grid     




       if row[i] == "?" and not visited[(j)]:  

            visited.append()               
             result = max([x,y], key=grid) # Find maximum initial from current cell 


           else:      # If there is no empty space or it has already been filled with another initials then skip to next row    



              continue     




   return result  

for _ in range(int (input())):        ## Number of test cases       
         R, C = map((lambda x : int()), input().split)      # Dimensions 


          grid= [[row[i] for i],range()] # Create grid from the inputs    



     visited=[]  

   result=[""]* R*C            




        for row in range(len (griod)):       ## Iterate over rows of cake         
           print(*map((lambda x : result if visited else "?"),grid))      # Print decorated cakes with initials