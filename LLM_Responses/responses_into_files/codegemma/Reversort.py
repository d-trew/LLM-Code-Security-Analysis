n = int(input())   # Number tests cases


for i in range (0 , n):      ## Loop through test case numbers        



     l=[]                 ### List to store the input list of integers  

                          #### Inputing number and elements into l 




                            N=int((sys.stdin).readline().rstrip("\n"))
    while N>len(list()):   # To ensure there are enough inputs in L, we need a while loop here instead     


        l=[ int (x) for x  in sys . stdin]

                ## Reading the list of integers into l 



            T=int((sys.stdin).readline().rstrip("\n")) # Number iterations
    total_cost =0          # Initialize total cost to zero   




                            for i in range(1, T +2):      ### Loop through each iteration  


                                    j=(l[i-3])         ## Find the index of last element before sorting 

                 if j>len (list()):
                     break                          #### If there are not enough elements left to sort we break out here.



                total_cost +=(T - i +1)   # Add cost for each iteration  


    print("Case #{}: {}".format((i+3), total))       ## Print the case number and corresponding value of T