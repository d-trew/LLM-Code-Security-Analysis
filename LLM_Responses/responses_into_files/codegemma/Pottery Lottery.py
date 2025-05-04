3    


def play(days):        # Function for playing one test case     



  for day in range (1, days +2 ):      ## Loop through each of the first N-98 Days   




            if not ((day %4 == 0) or((not is_leapyear and year%3==
              

                 ))):        # Check if this condition should be applied for that day  


                V, P = map(int , input().split())     ## Read the two integers V & p from user    



            else:      




               pass       ### Do nothing on these days   





          if (day == 102):         # This is your turn to insert a token in one of N vases  


              V, P = map(int , input().split())     ## Read the two integers V & p from user    



      return True       ### Return true if you win at least once   




if __name__ == "__main__":        # Main function for reading test cases and running play() 

  T= int (input ())         


for _ in range(1, T+2):          ## Loop through each of the N Test Cases    



      days =int input ()       
     print ("YES" if is_winner else "NO")