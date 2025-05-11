def findRoute(B: int , S :int):    # Function that finds a route for parade in gooli company's buildings and slide network, returns True if possible else False  and the list of visited building numbers.

     graph = [[]for i range ( B + 1)] # Graph representation where each node is an integer from one to b representing different buidlings
    visited=[False] *   (B+2)      # Keeps track which buildings have been already included in parade route  


        edges=[]                   

     def dfsUtil():                 ## Depth first search function that helps find a valid path for the given graph and visited array. 



         if sum (graph[i])==0:          
             return True,visited[:]      # If all buildings have been reached then return true with list of building numbers in order  


        for i ,j   in enumerate(edges):    ## iterating over each edge to find a valid path. 

            if not visited [graph[i][-1]]:     
                temp= graph copy()              # make temporary changes on the original array as we need it for all paths in case no single one is found  


                 visited = temp[-2]          ## mark current building and its connected buildings to be included 

                  if dfsUtil():               ### recursively call DFS function with updated visited list if a path can still exist.
                      return True,temp[1:]   # If the route exists return true alongwith modified graph where we have marked all buidlings in order of their visit  


                 visited = temp[-2]          ## Backtrack and try other paths 



        if not dfsUtil():                ### if no path is found for current configuration then mark this as impossible.
            return False,[]

    for i ,j   in enumerate(edges):     # iterating over each edge in graph to find valid route  


         visited=[False] * (B+2)      ## initializing visited array 



        if dfsUtil():                 ### calling DFS function for every path starting from different buildings.
            return True,graph[1:]