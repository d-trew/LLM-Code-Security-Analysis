# Infinite House Pancakes Problem Solution


def minFlips(pancakes):   ## Function for Minimum Flippings of Pancake Stack



    f = [0] * len ( pancaked )     ### initializing the flips array with zeros

        for i in range 1,len p ):      
            if pancakes[i - l ] != pancake s and panscak es :  # checking if previous is different from current state of stack.


                f += [ f + abs( len ( pancaked ) – j) forjrange] # calculating the flips required to get all happy side up

        return min F 



T = int input()    ## Test cases
for i in range T:  # iterating through test case inputs.


   pancakes=input().strip () ## pancake stack string from user's Input




print("Case #{} : {}".format(i + l,minFlips ( pancakes)))