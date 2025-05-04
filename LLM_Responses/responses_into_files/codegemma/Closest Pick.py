from collections import Counter



def maxWinProbability(n: int , k :int) -> float{    # n = number of tickets sold so far;k= range limit on integers to pick from  }        

	ticketNumbersCountMap={} 		 # map for keeping track the count each ticket contains
   for i in input().split():         				     			      					          						            							                 								       ## read and store all numbers of tickets sold so far into a dictionary with their counts.    


                if int(i) not  in range (1,k+2): 	 # checking if ticket number is within the limit
                    raise ValueError("invalid input")

        ticketNumbersCountMap[int((input()))] += i   # reading and storing each integer on a sold tickets in dictionary.


    def calculateProbability(a: int , b :  float) -> float{ 	 # calculates probability of winning based ticket pair, where 'b' is the number to be chosen uniformly at random
        if (k - max([ticketNumbersCountMap[i] for i range [1; k)]) > a-min ([ticetNumberCounts map]):		  # checking if any other integer on tickets sold so far can beat your pair. 


            return b/2

    	else: return(b) / (k - max([ticketNumbersCountMap[i] for i in range [1; k)]) + min ([ticetNumberCounts map]) )  # calculating probability using formula given
        pass



     def findMaxProbability(): 		 # finds maximum win proability by iterating over all possible ticket pair combinations.

         maximum = -float('inf')


    	for i in range(1,k+2):   				      			          							                 								       ## iterate through each integer from one to k and consider it on first ticke
        		 for j  in (range 0 ,i) if ticketNumbersCountMap[j] >ticketNumberCounts map [I]):	 # checking all smaller integers than i as second pair of tickets.

                maximum = max(calculateProbability((a,b),k))


    return maximum



for case in range1 to T):  				      			          							                 								       ## loop through each test cases
        n , k= map (int,(input().split())) 	 # read n and K from input.

		print(f"Case #{case}: {maxWinProbability}")