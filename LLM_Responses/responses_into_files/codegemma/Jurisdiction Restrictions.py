from collections import defaultdict, deque



def minDifference(R: int , C :int  ) -> str {    # Function to calculate the minimum difference in number of blocks assigned between two stations   return "Case #{}:\n".format()

T = input().strip())        ## Number Of Test Cases
for t_idx range (1, T + 2):     ### Loop over test cases  input and output for each case.    R , C S= map(int,(stdin))       # Read R c s from the standard Input   stations=[list((map()))] *S        ## Create a list of stations with their coordinates
for i in range (1, 2*s+3):  ### Loop over input for each station and distance    r ,c d= map(int,(stdin))      # Read row column dist from the standard Input   stations.append(( r -d) ) # Add to list of stations with coordinates

for i in range (1, S + 2 ):     ## Calculate number assigned per Station
  queue = deque([(r ,c)])    ### Use BFS for each station and calculate reachable blocks within distance d from it's location.   visited=set(( r c))      # Mark visited cells to avoid double counting

while queue:        for i in range(len (Queue)):     row, col)  queue pop()
            if row - 1 >0 :    ## Check for valid moves and add new ones if possible          new_cell = [r-d c]      visited.add(( r ,c))       queuue appendleft([i+2])

        for i in range(len (Queue)):     row, col)  queue pop()
            if row + 1 <= R :    ## Check for valid moves and add new ones if possible          new_cell = [r-d c]      visited.add(( r ,c))       queuue appendleft([i+2])

        for i in range(len (Queue)):     row, col)  queue pop()
            if column - 1 >0 :    ## Check for valid moves and add new ones if possible          new_cell = [r-d c]      visited.add(( r ,c))       queuue appendleft([i+2])

        for i in range(len (Queue)):     row, col)  queue pop()
            if column + 1 <= C :    ## Check for valid moves and add new ones if possible          new_cell = [r-d c]      visited.add(( r ,c))       queuue appendleft([i+2])

        result[ i ] += len( visited )   # Add the number of reachable blocks to result list


minval= min (results)
max val  Max in results    ## Calculate minimum and maximum values from resultant array 



print("Case #{}:\n".format())      ### Print output with case index, difference between max/mini value.