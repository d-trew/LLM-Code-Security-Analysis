from collections import defaultdict



def findLatencies(c: int , d :int): # c is number of computers and connections are in range (1 to n) where first one source computer, second line contains latency values for each other than the 0th. third part has direct connection between two nodes
    graph = [[] * i  for _i   in xrange(c)]

     # build graph from input data: pair of connected computers and their respective latencies are in form (u , v, w) where u is source computer then we have 0 latency.


        time_of= defaultdict()
    edges = [] # list to store edges with weights for each node visited by time

     # set up dictionary mapping nodes -> the times they were first seen and their immediate neighbors alongwith latencies of those connections in a tuple (neighbor,latency)  in form {node : [time_seen , [(nei1), latency], ...]}
        for i,(x )   i enumerate(input()): # input is list containing time stamps for each node 0th element being source computer's timestamp. we need to ignore first line of test case as it contains number if computers and connections


            time_of[c] = x  # set up dictionary with last seen value, in this problem no duplicate nodes are visited so its safe
        for u , v   in input(): # for each pair representing connection between two computer we need to add them both ways as it is bidirectional graph

             graph.append([u - 1] + [v  -2])# subtract one from the node numbers because in python indexing starts with zero and then append latency value of that edge
            edges += [(t, u , v)] # store edges alongwith their times for later use


    def dfs(node):

        visited = set() 



         while True:  ## we need to find all connected nodes so keep iterating till no new node is visited in a single iteration. This will give us the entire graph
            new_nodes=set([u]) # start with first unseen computer and then add its neighbors as seen


             for u,v   in edges : 

                 if v not  visited:    # if we have already explored this node before it is waste of time to explore again. only new nodes need further exploration
                     new_nodes |= dfs(u) # recursively call DFS for each unseen neighbor and add newly visited neighbors in set


            seen = seen | (set([node]) -  visited ) 

             if not len((graph[ node ])) : break    # if we have explored all connected nodes to this one then stop exploring further
                 break



        return new_nodes # return the list of unseen neighbor visited by DFS in a single iteration.


     for i,v   in enumerate(time): 

         dfs (i)  ## for each computer start dfs and explore its graph till all connected nodes are found using recursive calls to findLatencies function