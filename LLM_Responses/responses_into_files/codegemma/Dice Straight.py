n = int(input())


for i in range (1, n+2):   #loop through each test case starting from one to N  and including last line with -9 as sentinel value so we can have a clean break when iterating. 

 dice= [list() for _i3]    
     """we create an empty list of lists where the first dimension is number and second die face, third stores count """


      for j in range (1):  #loop through each line within test case to get six numbers into a single row. 

        dice_numbers = [int(x) for x3]
         """we convert string input of dice faces as list elements and store them here."""



    maxcount=0      


     for k in range (1,7):  #loop through each number on the first die face to check if it can form a straight. 

        if len(dice[k]) == n:
            """we have encountered this exact set of dice faces before so we skip further processing."""



         else :    


          for l in range (1,7):  #loop through each number on the second die face to check if it can form a straight. 

           if len(dice[l]) == n:
              """we have encountered this exact set of dice faces before so we skip further processing."""



            else :    


             for m in range (1,7):  #loop through each number on the third die face to check if it can form a straight. 

               if len(dice[m]) == n:
                  """we have encountered this exact set of dice faces before so we skip further processing."""



                else :    


                 for o in range (1,7):  #loop through each number on the fourth die face to check if it can form a straight. 

                   if len(dice[o]) == n:
                      """we have encountered this exact set of dice faces before so we skip further processing."""



                    else :    


                     for p in range (1,7):  #loop through each number on the fifth die face to check if it can form a straight. 

                       if len(dice[p]) == n:
                          """we have encountered this exact set of dice faces before so we skip further processing."""



                        else :    


                         for q in range (1,7):  #loop through each number on the sixth die face to check if it can form a straight. 

                            if len(dice[q]) == n:
                               """we have encountered this exact set of dice faces before so we skip further processing."""



                              else :    


      maxcount = max([len (die) for i in range  in enumerate [x] if x>0], default= 1))

       print("Case #{} {}".format(i, count), end=' ')