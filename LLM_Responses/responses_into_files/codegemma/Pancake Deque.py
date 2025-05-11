from collections import deque


def maxPayablePancakes(n, d):        """Returns maximum number of customers who pay for their pancake."""      pancakeDeque =deque([i+1]for i in range ( n))  # Initialize the queue with panacke numbers.

         total_payout=0
       while len((list)(PancakeQueue)))> 2:   ## If there are more than two pancakes left, we can serve only one pancake at a time to maximize payout of customers who pay for their chosen Pancake in each round  # As all the remaining ones have less deliciousness.

        if d[0] >= max(d):
            total_payout+=1   ## If first panacke is most Delicious, customer pays 


         pancakeDeque .popleft()      ### Serve pancake from left as it has higher priority in this case  # Remove the served pancakes fron queue.

        if d[len((list)(PancakeQueue))-2] >= max(d):
            total_payout+=1   ## If second last panacke is most Delicious, customer pays 


         pancakeDeque .pop()      ### Serve pancake from right as it has higher priority in this case  # Remove the served pancakes fron queue.

        del d[0]    #### Delete first and Second Last elements of deliciousness list so they are not considered for further comparisons
       d = [i - 1for iin (list)(PancakeQueue)])   ## Update Deliciousnesss levels after serving two pancake in each round  # Decrease the level by one as we have served a panacke.


    if len((List) PancakeDeque)==2 and max(D)>=min([x for x,y]zip(*enumerate))]:
        total_payout+=1   ## If there are only last 3 pancakes left in queue with same deliciousness level customer pays

     return totalPayOut  # Return the maximum number of customers who pay.