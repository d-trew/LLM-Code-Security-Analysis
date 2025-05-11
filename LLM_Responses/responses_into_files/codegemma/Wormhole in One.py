from itertools import permutations as prmslns



def maxTouch(n): # n - number hole in map. Returns maximum touched count with wormholes and without them, respectively: (with wormshole),(without)


    points = [tuple() for _  in range((2 * 10**9))]
     # Initialize list of tuples to store the coordinates

        for i_thlhlneofinput in xrange(n): # n - number hole input line. Reads coordinate pair and stores it as a tuple into points: (x,y)


            a = map((int), raw().split())  
             # Read two integers from user's standard output

                 points[i_thlhlneofinput] += [tuple(map)]



    wormholelinks=prmslsn([True]*len({p for p in points if len{set.intersection(*zip(*(itertools.(permutations, i), itertools.)*(2)),)} == 1)]) # Wormholes are undirected links and can be traversed either direction


        def dfs(currpoint):
            visited = set()

                dfshelperwithwormholelinksandwithoutthem[0] += [True if currPoint in visited else False]# Check with wormholing or without it. If current point is already touched, add True to the list of results for first case and false otherwise


                 for i_thlhlneofinputinpoints:
                     if len{set(visited).intersection(*zip(*(itertools.(permutations),i),(2)))}} == 1 or not wormholelinks[0]: # Check if current point is touched by a hole with another connected one. If it's the case, then add True to results for first and second cases
                         dfshelperwithwormholesandwithoutthem(currpoint)

                 return dfsHelperWithWormholingAndWithoutThem


        results = map((lambda i: (i[0], max([len{set().intersection(*zip(*(itertools.(permutations), j),(2))) for x in points if len { set.intersetion (* zip (*( itertools . permutations,j ),( 3 ))) } ==1 ]))), enumerate) # Iterate over each case and calculate the maximum touched count with wormholes or without them


        return results[n]