from heapq import heappop as pop    # priority queue operations (heapq) are faster than list sorting in this case  



def solve(R, B: int , C :int):   ## R robots ;B bits;C cashiers

        cashier = [0] * 128
                for i,_,(Mi_, Si_),(Pi_)in enumerate([list() for _i__j in range (3)] + [[M*Si, Pi]]*(R)):  # cashier setup with max capacity and time per bit/pay

                        cashier[C-len(a)].append((Ti_/B)+1) # adding the cashiers into priority queue based on their work duration for B bits
                ans = 0; heapify (casher);    ## we start from zero seconds, so ans is initially set to be at least equal of that

        while R:  # while robots are still alive and have tasks left in hand. Time complexity O(R*logC) where C - total cashiers
            t = pop() # robot with minimum time required for cashier interaction 


             if t > ans :ans=int (max((a,b),key=(lambda x:x[1])) [0])  # we need to consider the maximum duration of work by any robots while interacting.

                 R -= R and B >=t
                B-=r * r # robot finishes its task with time t 


        return ans



if __name__ == "__main__":    ## main function for input/output handling in python  (not required)   for other languages it might be necessary to have this part

            T = int (input())
                ans =[] ; i=0;     # we need answer list and index of test case 


                 while T:        ### loop over all the cases as defined by input format. Time complexity O(t*R * logC) where t - total number  of tests

                    i+=1    ## incrementing to track current Test Case
                        l = [int (x ) for x in list((input().split()))]   # reading R,B and C values 


                            ans.append("Case #{}: {}".format( i , solve(*[ int(_)  for _j_k__v3456789012 ])))

                        T-=t    ## decrementing total number of test cases left to be solved
                print("\n".join([str(_a) for x in ans]))   # printing the results