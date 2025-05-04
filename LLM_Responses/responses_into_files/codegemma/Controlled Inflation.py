# Python code for gas station pump optimization


def minButtonPresses(N: int , P :int):   ## N - number of customers, p-number pf products per customer.    products = [[0] * (P +1) ] # list comprehension to create a 2D array with n rows and  p+l columns
for i in range((n)):

     # Read the target pressure for each product from user input as an integer, store it into elements of products[][] using nested loops.    products[i][j] = int(input())


minPresses=0 # initialize minimum presses to zero 



def pumpProduct (targetPressure:int):  ## function that takes a single target pressure and calculates the number pf button press required for inflation
     currentpressure, countpressess , changeindirectionofpumping   # current pascals of product after pumping up or down.

    while True : # loop until we reach desired state 


        if (targetPressure >  changeInDirectionOfPump):            ## if target pressure is greater than the direction in which pump was moving then press it further
             currentpressure += countpressess   # current pascals of product after pumping up or down.

              countPresses+=1 # incrementing number pf presses by one 


        elif (targetPressure < changeInDirectionOfPump):  ## if target pressure is smaller than the direction in which pump was moving then press it further
            currentpressure -= countpressess   # current pascals of product after pumping up or down.

              countPresses+=1 # incrementing number pf presses by one 


        else: break ## exit loop when we reach desired state  ## if target pressure is equal to the direction in which pump was moving then press it further
    return countpressess



for i, productRowinProductsList In enumerate(products):

     totalPresses=0 # initialize total presses for each customer products 


      # iterate over all of customers and their respective porducts  ## sum up the number pf button pushes required to inflate a single user's worth
    Totalpressess+=sum([pumpProduct (targetPressure)for targetpressure in productRowinProductsList[1:]])

     minPresses=max(total presses, min Pressesses ) ## update minimum pressses for all customers 


print("Case #{}: {}".format((testCaseNumber), totalpressed))  ## print the case number and minimize pressed buttons.