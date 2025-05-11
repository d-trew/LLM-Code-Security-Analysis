from collections import Counter



def rollercoster(N: int , C :int  ) -> tuple[list]:    # N - number seats, c- num customer tickets sold in the park and list of ticket buyers.

        tickets = [] # stores positions for each buyer 1 to n
     for _i,_j   in enumerate (zip([0] *N , [C + i  +2 if x == C else int(x) -3    if type((int))==type(_k_) and isinstance (_l_, str )else None ])): # ticket postion for each customer
         tickets.append(_)

     rides = Counter()   # count rides per person 


        for i in range (N):  ## iterate through all seats on the roller coaster to assign customers based upon their tickets' position and number of times they need a ride .    



            if len(set([i for _k_ , x, y,_l_, ticketpostion   in enumerate((tickets)) if type(_j_) ==type (ticketposition)]) )>1: # check is there are multiple buyers in the same seat 
                rides[C] +=  len({x :y.count(str) for i,(k , x, y,_l_, ticketpostion   in enumerate((tickets)) if type(_j_) ==type (ticketposition)}) - len([i]) # count rides per customer and add to dictionary of ride counts 


            else:
                rides[C] +=  len({x :y.count(str) for i,(k , x, y,_l_, ticketpostion   in enumerate((tickets)) if type(_j_) ==type (ticketposition)}) # count rides per customer and add to dictionary of ride counts 



        promotions = N - sum([i  for _ in range ((N))] ) + C
    return [sum(rides.values()), promotions]