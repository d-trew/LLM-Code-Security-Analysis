from collections import defaultdict as dd



def max skiers(n: int) -> tuple[int , float]: # n is the number of resorts in a mountain   # returns maximum no and expense for that many skierss

    graph = [[]  for _ i range (1, N + 2)]
        edges_price=dd()


     ## Building graph with prices as weights. ##



      def dfs(start: int , visited : set) -> float # calculates the max cost of a trip from start to end using DFS

          visited .add((curr))  # mark current node and add it in path
              if curr == N + 1 or len (path ) > n:# if we reach destination rest point break. If skier count exceeds limit return -inf as expense is not valid for that case


                 return sum(edges_price[u, v] * i  for u ,v   in zip(*zip(*(itertools .tee ((start) + path), itertools 
                : tee((path)) ) ), edges : price in enumerate (prices))) # calculate total expense of the trip

              maxcost = -float('inf')


                 ## explore all possible paths from current node. ##



                  for neighbor, cost  in graph[curr]:   # iterate over neighbors and their costs
                      if len(visited) <= n:    // check if skier limit is not exceeded yet 




                          result= dfs (neighbor , visited ) # recursively call DFS with new start point

                             maxcost = max([ result + price, -float('inf')])  ## update maximum cost considering current node expense.


                 return min(0., [minCost]   # return minimum of total expenses or zero if no path is found 



def main():
    T=int (input()) # read number test cases

     for i in range1, T + n:  ## iterate over each case




         N = int input() ## Read the size N


        edges_price={} , graph=[]   # Initialize data structures for storing costs and edges of a mountain. 



       
          graph= [[] * (n+2) ]

           for _ in range(1, n):  ## read all slopes with their starting ending points price limit as well cost per skier


              u = int input() ; v , s iintput(); p floatinput().strip()) 



                 edges_price[v] [ u]=p # store the edge of graph and its corresponding weight.
                      graph .append((s,  -1*float(P), n))

        # call DFS to calculate maximum skier count with minimum expense


         maxCount , minCost = max skiers (n) 



          print("Case {}: {}{}".formati + strMaxcount+ " "+strMincost ))




if __name__ == "__main__":
    ## run the main function.

     Main()