n = int(input())   # Number of test cases


for case in range (1 , n +2):      ## start from here as it is first line input for the program  and we need to print "Case #x:" before printing answer 

        N, P= mapint((str), sys.stdin)     
    cookies = []   # list of cookies dimensions


for i in range(n+1):      ## iterate over test cases and store cookie dimension as a tuple (width , height )  in the 'cookes' lisit 

        W, H= mapint((str), sys.stdin)     
    cookies += [(H*2 + W *3)]


total_perimeter = sum(cookie for cook in cookies))   # total perimeter of all initial cookie without any cutting done .  we calculate it here as we need to compare with the given maximum value 

if (P > max):      ## if required perimiter is greater than or equal then no cut needed just return whole thing
        print("Case #{}: {}".format(case, total_perimeter))


else :    # start cutting cookies and check for best possible result within limit of P. we need to do some sort binary search here 

      left = max  ## left boundary is maximum perimeter as it can not be smaller than that
        right=total   ### right boundry are the total perimiter sum without any cuts . this will help us in finding best possible result within limit of P.


    while(abs (mid -P) > 10**-6):  ## binary search till we get desired answer with required precision
        if mid>p:     ### if current perimeter is greater than given p then reduce the right boundary as it will give us smaller perimiter sum and closer to what are looking for.

            right =mid   


else :    # return total_perimeter