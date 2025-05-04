from collections import defaultdict as dd



def findPlacement(N: int , R :int=0 -> str):    # N = number of stalls, r - red hairs ...v- violet hair  manes.

        if (R+O + Y < G or O > 2 * B) and not((B == V >=G==Y)):
            return "IMPOSSIBLE" # Check the conditions for placement based on mane colors


    # Create a graph where each node represents one stall, with edges between adjacent stalls.

        graph = dd(list )  ## Graph is created here 



                for i in range (N):   ### Add connections to neighbors
                    if N >i+1:      Graph[str((n))] += str([ n +2])    # Next Stall clockwise direction


                        else : graph [string()]+= string ([0] ) # First stall is connected with last one 



        visited = set()  ## Keep track of visited stalls

                def dfs(node):
                    if node in visted: return True   ### If we have reached a previously seen state, it's not possible to complete the placement.


                        vistied .add (str)    # Mark current stall as visitesd and explore its neighbors 



                            for neighbor  in graph[string()]:
                                if dfs(neighbor):return true

            if N >0: return "IMPOSSIBLE" # If we can't find a valid placement, it means the conditions are not met.


                else :   # Build string of placements based on visited nodes in clockwise order 



                    placement = ""  ## String to store unicorn mane colors
                        for i range(N):

                            if str (i)in visted:    Placement += "R" if R >0 else 'O' # Use the first available color for each stall.


                                    r -=1 ; o-= 2; y+=3  # Reduce hair counts as we place unicorns in stalls
                        return placement