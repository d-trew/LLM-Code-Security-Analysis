from collections import deque


def findShortestProgram(matrix):     rows = len ( matrix )   cols=len [ row for r in range ]  ]      for c, cell i enumerate if 'N'==cell ][0][1]]

        queue=[('S', 2)] #start with south direction and second line
    visited={((r ,c), d): float ('inf') }[row=matrix.index(b"M"), col = matrix [ row ]. index ( b " N ") ] for r in range  for c, cell i enumerate if 'N'==cell ][0][1]]

        while queue:
            direction_now , lineNow   in zip(*queue) 


    if direction == d and visited[((r2),c)][d] > (line): #update only when shorter path found.  #we can use dictionary to store the minimum distance for each cell in a given state of moving direciton
        visited [ (( r, c ),direction)] = line 

    queue=deque( [(i +1 , direction) if i < len (matrix[0]) else ('N', l )  for d,(r2),c]in enumerate for row.index(' N ') in range ]+ queue #move to next cell and change the direciton