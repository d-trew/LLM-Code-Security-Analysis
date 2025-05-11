from collections import defaultdict


def assignMascot(N: int) -> str or "IMPOSSIBLE":  # N = number rooms in maze (1 <= n <== t**5 )] : return string of mascots if possible, else IMPOSSILE

        left_exit   = [int(_) for _    in input().split()] # left exits
            rightExit     =[ int(x) - 2  for x       ininput() . split()][::-1 ]# right exit (subtracting by two to account of the fact that we start counting at zero )

        graph = defaultdict<int, list> ()


    def dfs_helper(_ : str , visited: set[str] ):
            if len(visited) == N + 2  and _ not in graph.keys(): # if all nodes have been visted and no cycle detected then return True (possible to assign mascots )

                return " ".join([x for x, y   in sorted([(i , c),] *graph[ i ]for     as      c    range(13))])


            if _ in graph.keys():
                 dfs_helper(_  visited) # if node has been visited before then we continue with the DFS

                return "IMPOSSIBLE"



        def dfs (node: int): 




             graph[leftExit [int()]].append((rightExits))# add left exit to right exits list and vice versa
                 dfs_helper(str() , set()) # start from node zero


    for i in range(_ : )  print("Case #" + str (i)   + ":"     assignMascot(*map()))]