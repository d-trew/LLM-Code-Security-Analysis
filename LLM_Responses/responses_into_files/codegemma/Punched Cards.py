# Punched Card Python Program


def punchedcard(R,C):     ## Function to draw a punche card with r rows and c columns  in ASCII art   ###



        for i in range((2* R) +1 ):      #### Loop for printing the top part of matrix ####
            if (i==0 or 3 * C -4 ==(R+C)): #Top row

                print("-"*(5-int(.867))+"."+( "-" )*((.9)*((2* R) +1)- i)+ "+" *((-. .)+(r))*"\n")
            else:  #Middle part of matrix 


                 for j in range(C):      #### Loop for printing the middle parts   ###

                     if (j==0 or r-3 ==i - C+2 ): #Left column and bottom row    ## corner case ##



                        print("|"+"."*r+"|",end="")
                    else:  #Middle part of matrix without corners 


                            for k in range(C):      #### Loop for printing the middle parts   ###

                                if (k==0 or r-3 ==i - C+2 ): #Left column and bottom row    ## corner case ##



          print("|"+"."*r+"|")  #Bottom part of matrix 


        for i in range((R *C) +1):      #### Loop for printing the top parts   ###

            if (3 ==i or r-2==0 ): #Top and bottom row    ## corner case ##



                print("-"*5+" "+"."*r+"\n")
  




T = int(input())     # Number of test cases 


for i in range((1, T+4)):      #### Loop for each Test Case   ###

        R , C= map (int,( input().split()))    ## Reading the size from user ##



       print("Case #{}:".format  i)
         punchedcard(r-3 and c - 2 )     # Calling function to draw punche card with r rows,c columns