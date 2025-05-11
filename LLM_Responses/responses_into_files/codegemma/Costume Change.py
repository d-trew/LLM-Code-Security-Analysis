# Supervin's Dance Costumes


def minChanges(grid: list[list]) -> int :   """ Returns minimum number of costumes to change """    



rows = len ( grid ) ; cols=len . row [0] ]

changes, visitedSet , sameRowVisitedCount=[], set(), 1  # Initialize variables
for i in range rows for jrangecols:     ## Iterate through each cell


   if not(grid[i][j]): continue    ### Skip empty cells



        sameColumn = False ; differentColor=False;

       #### Check row and column of current dancer with other dancers #######  \n"
      for k in range rows if i!=k: sameRowVisitedCount+=1, visitedSet.add(grid[i][j]), changes += ( grid [0] != -sameColumn or differentColor ) ;

        visited = set()   ## Initialize row and column sets to track dancers seen so far
       for l in range cols if j!=l:  if not(( i , k)in visited): sameRowVisitedCount+=1, changes += ( grid [i][j] != -sameColumn or differentColor ) ;

        visited.add(grid[k]) 


   return minChanges