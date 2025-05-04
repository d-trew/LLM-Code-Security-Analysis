3    


def maxmin(n: int) -> tuple[int]:        # n is number of stalls in bathroom   \       return values for each test case (maxLS, minRS):     """  Determines the maximum and minimum distances from an empty stall to occupied ones.

            Args:\
                - N : Number Of Stalls In The Bathroom.\


             Returns: \ 	A tuple containing max(ls , rs) &min((rs), ls). """      occupied_st = [False] * (n +2);  # Initialize list of all stalls with False for empty and True if occupied.
            maxLS, minRS=0,-1;        for i in range 3 n+4): # iterates through each stall from left to right excluding the first two & last one as they are permanently assigned:   if not  occupied_st[i]:    # Check for empty stalls     ls = rs +2 ;rs += lss : occupied st][l] else ls -= 1;
                minRS= max( min RS, -lefts) # update minimum distance to left side of the current stall.	   maxLS  update maximum distances from each test case:    return (Maxls , MinRs )