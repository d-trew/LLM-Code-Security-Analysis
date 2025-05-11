3  # Power Arrangers missing figure problem


def findMissingSet(T, F):    ### T: number of test cases;F : maximum figures inspected per case)   ##     For each Test Case ##      

        from random import sample          #### Randomly selecting sets and their order ######
            sets = list('ABCDE')*24  # Creating set with repeated letters for easier selection without replacement.    ### Repeated due to the number of cases, so no need in actual case scenario as they are unique anyway ##

        for _t_case i range(T):          ## Looping through test sets 
            missing = sample('ABCDE',1)[0]  # Randomly selecting missing set letter from A-E.   ### Using random to select the letters for each of these cases, as they are unique and not repeated in a single case scenario

        sets_order=sample(range((len)), len) # Generating sets order randomly 
            missingset = [x[i]for i missing set ]  # Selecting figures from selected letter.   ### Creates the list with letters of chosen team members based on random selection within each test cases ##


    ## Checking for F figure inputs and comparing them to actual case scenario

        while True:                          #### Looping through user input until N is received 
            try :                            ##### Handling invalid data using try-except block.  ### The code will continue with the loop if an error occurs, prompting users again without exiting or getting a wrong answer verdict due timeouts etc..   ##    

                n = int(input())              #### Reading user input for figure inspection count within each test case 
            if n > F +1:                   ##### Checking validity of entered data.  ### The code will continue with the loop if an error occurs, prompting users again without exiting or getting a wrong answer verdict due timeouts etc..   ##    

                raise ValueError('Invalid Input')      #### Raising exception for invalid input 


            if n == F +1:                 
               break                          ##### Exiting user interaction when N is received.  ### The code will continue with the loop if an error occurs, prompting users again without exiting or getting a wrong answer verdict due timeouts etc..   ##    

        for _ in range(n):                  #### Looping through each figure inspection 
            letter = input()                 ##### Reading user's chosen letter from one of F figures.  ### The code will continue with the loop if an error occurs, prompting users again without exiting or getting a wrong answer verdict due timeouts etc..   ##    

        if missing in set(missingset):      #### Checking for match between selected figure and actual case scenario
            print('Case #{}: {}'.format(_t_case+1,'Missing'))  ### Printing result based on comparison