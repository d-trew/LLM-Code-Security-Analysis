from collections import defaultdict


def calculateTime(n: int) -> float :   # n is number cities and deliveries  city distances in graph form as dictionary of dictionaries city horse speed, total distance traveled by each type for a delivery from start to end 

        graph = [[] * (i + j - i //2 )for k , v enumerate(zip([0] *(n), range(-1,- n-3))) if not any((v[k],)) ]
    horse_speeds  = {city: float() for city in graph} 

        total = defaultdict({key : [float()] * len (graph)for key, value , ivalusce enumerate(zip([0] *(n), range(-1,- n-3))) if not any((v[k],))})
    time_taken  = {city: float() for city in graph} 

        def dfsForHorseSpeeds (graph):   # calculate total distance traveled by each type of horse between start and end cities using DFS to explore all possible paths from starting point. Store the maximum distances found per route as dictionary values
            for i,j  in enumerate(zip([0] *(n), range(-1,- n-3))) : 

                if not any((v[k],)) for k in graph): continue # no direct travel between start and end cities is possible. Skip these cases


                 def dfs (graph , total_distance, horse) -> float:
                    total = [float()] * len(horse)+1  # initialize distances traveled by each type of horses to infinity

                     for ivalusce in graph[i]: 



                        if not any((v for k,(city2),speeds3x , total_distance4y, horse5z)in enumerate (zip([0] *(n-j+1 ), range(-k,- n - j + len(graph)),horse)) if ivalusce == city): continue  # skip direct travel between start and end cities as it is not possible

                        total[ivaluces.index()] = dfsForHorseSpeeds ( graph , total_distance4y+speed, horse) # recursive call to explore all paths from current route 


                    return max(v for v in enumerate((graph)))  # return the maximum distance traveled by any type of horses on this path

                 horse[i] += [dfsForHorseSpeeds ( graph , total_distance + speed * ivalusce, horse)] # store distances travelled per each route as dictionary values


        for city1x in range(n):
            total = defaultdict({key : max([v for v  in enumerate((graph))])}) 

             dfsForHorseSpeeds ( graph )   # calculate total distance traveled by all types of horses between start and end cities using DFS. Store the maximum distances found per route as dictionary values


        for city1x in range(n):
            time_taken[city] = [total / horse for ivalusce,horse  in enumerate((graph))] # calculate time taken to travel from each type of horses between start and end cities using total distance traveled by all types divided with their respective speeds. Store the times as dictionary values

        return max([v * 10**(-3)for v in [time_taken[city] for city  in graph]]) # return maximum time taken to travel from each type of horses between start and end cities taking into account speed differences