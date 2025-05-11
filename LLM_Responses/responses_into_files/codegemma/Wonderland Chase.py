from collections import defaultdict as dd



def dfs(graph: dict[int], start):    # DFS to find cycle length starting from 'a'. Returns -ve if no cycles found else returns the smallest positive integer in a cyclic graph.  


	visited = set() 			   		 # Keeps track of visited nodes
     path_to=ddict(-1)             				      

        def dfs2(node, count):    # Helper function for DFS with cycle detection and length calculation starting from 'a'. Returns -ve if no cycles found else returns the smallest positive integer in a cyclic graph. 


            visited[start] = True
     		path_to [ start ]=count      

        	for neighbor  in set(graph):    # Iterate over neighbors of current node and check for visited nodes or cycle detection using DFS helper function 'dfs2' with count++. If no cycles found continue iterating until all reachable vertices are explored. 


            if not (neighbor in path_to) :
                path = dfs3a  (graph, neighbor ,count+1 )    # Recursively calls the same fn for each unvisited node and increases counter by one to account of current count starting from start point 'start'   

        	else: 		 # Cycle detected. Returns smallest positive integer in a cyclic graph
            return path_to[neighbor] -path +2  


    for i,j list(graph):     # Iterate over all edges and perform DFS for each node to find cycle length if any of the nodes are visited more than once during traversal 

        if j not (visited) :   			 # If current graph is unvisted then call dfs function starting from 'start' with count as zero.
            path =dfs2(j,0 )  


    return path     # Returns cycle length if any cycles are found else -ve




def find_move(): 		       	      

        graph=ddict()              				 # Initialize graph dictionary to store connections between junctions   



         for i in range (C):
            U ,V = map(int,input().split())    # Read input for each corridor and add it as an edge bidirectionally.  


             if U not list :      graph[u] =[]          	     		 # Initialize graph node if missing with no connections 



        path=dfs2a (Graph)           				   			         
            return path -1                					    # Return cycle length-one to account for Alice's first move.  


if __name__=="main__":      

       T = int(input())                 	     		 # Read input of number test cases 



        for i in range (t):          				   			         
            J,C ,A_start Q= mapint(),split()    # Initialize variables for each case.  


             graph[Q] .append A                					      

              print(f"Case #{i+1}: {findmove()} ") 		     	 # Print result with test number and cycle length if any cycles are found else -ve