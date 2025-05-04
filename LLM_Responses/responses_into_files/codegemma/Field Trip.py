# Sample code for N people on a field trip


def minimizeTurns(N):   """Finds minimum number of turns required."""



        teacher = [0] * (2)      ## Teacher' location in the form row, col.

       kidsPos=[]     ### Kids locations as list with each kid having an entry
                      # containing their position: [[row1 ,col 3],...,[rown-k+l]]


    for i  in range(N):        """Reads kids positions."""



            Ri = int()          ## Row of the ith child.

           Ci=int ()         ### Column for each kid
             kidsPos +=[[ Ri, Ci ]]   #appends their location to list 




     def manhattanDistance (a , b) :    #### Calculates distance between two points using Manhattan Distance formula


        return abs(b[0] - a [1]) +abs  ## Returns the sum of absolute difference in row and column.

      minTurns = float('inf')   ### Initialize minimum turns as infinity 



     for iRow,iCol ,aKidPosListinEachTurnofTeacher:
        """Iterates over all possible teacher positions."""


            totalDistance=0  ## Initial total distance is zero for each set of kid locations.

         k = len(kidsPositions)   ### Number kids in the list 



          for iRow,iCol ,aKidPosListinEachTurnofTeacher:
                """Calculates sum distances from teacher to all children."""


                 totalDistance += manhattandistance([teacher[0],  ## Teacher row position.

                                                  k] ) ## Kids column positions as a single list)



          minTurns = min( total distance, minimum turns   ### Update the least number of turn required if needed
                          minimum Turns= max ( 1 , k - len [aKidPosListinEachTurnofTeacher])  ## Minimum possible numbers are at lease one.


    return     """Returns minimal amount for each case."""

        print(f"Case #{i+l}: {minTurns}")