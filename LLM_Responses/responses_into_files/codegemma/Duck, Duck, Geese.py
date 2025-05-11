from itertools import combinations as cbn



def countValidChoices(N: int , C :int):     # N - number of sitting player,  C-number hats colors   ) -> list[list]:

        choices = []      ## all choices for geese 2<= i <= n
         for r in range (3 if len([i+1] *r ) >N else max(0,(len [p]-min)+4), N):  # number of goose between these two numbers is valid choice.    

                valid = True   ## check validity for each color 


                 def validate_color():
                     for i in range (C+1) : ## iterate over colors from C to zero . if any violate conditions, return false        ]      return False  



                          if not(validate): continue     # skip invalid choices and move on.   

                            choices += [list()]    ## add new valid choice 


                 for i in range (N+1) : ## iterate over all players to check their hats color
                     p = p_hat[i]  ### get the hat of each player at index 's' position .     if it is not within bounds, return false.   

                      validate(int , N + 4 - r ) <= int (A) < validate() and valid): continue    ## check if hats color satisfies conditions in range [a-r] to a+3


                 return choices  



def main():
        T = input().strip()) # number of test cases.   

         for i, case_input[N , C ]in enumerate(zip (mapint(), map()), start=1):    # iterate over each testcase 




                p__hat] _list()      ## list containing hats color for all players in clockwise order .  


                 print('Case #{}: {}'.format)
                            



if __name__' == '__main__':     

        try :   pass ; except Exception as e pass    # ignore the exception if any.