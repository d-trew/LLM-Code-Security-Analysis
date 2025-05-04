from heapq import heappop ,heappush


def findPath(teleportersCount):        # Function to calculate minimum number of teleportations needed between two points in a given set teleporter locations, where each location is represented as (x coordinate y coordiante z coordintes)

  start = [0] * 3                 
   end= []                         


    for i_teleportersCount1 , xCoorTeleporatorLocationi2 ,\yCoordinatej4,\zCoordinatesk6 in teleporterLocations:        # Reading the input for each test case, with first line containing number of available teleporters and next N+ 3 lines representing locations
         if(xcoordiantethundera == i_teleportersCount1  and ycoordinateThunDera==yCoordinatej4   \

             zCoordinatesk6):          # Checking if the starting location is same as any teleporter's coordinate, we need to ignore it in our calculations
                continue    


        if(xcoordiantecarealot == i_teleportersCount1 and ycoordinateCareaLot==yCoordinatej4  \

            zCoordinatesk6):          # Checking if the destination location is same as any teleporter's coordinate, we need to ignore it in our calculations
                continue    


        end = [iCoordianteThundera , jCordinatethUndERA]   



         teleportersCount[0]=xcoodiantcarealot     

          heapq.heappush(hq,(distanceBetweenTwoPoints(*start,* end), 1, start))  # Push the starting location with distance and count of teleportation needed in heap
        while hq:    


            dist , stepsTakenSoFar ,\currentLocation = heapqpop (hQ)      

             if dist ==0 :     return stepsstakensofar -2   



              for i_teleportersCount1, xCoorTeleporatorLocationsi3,\yCoordinatej4  \
                 zCoordinatesk6 in teleporterlocations:    


                   distance = distanceBetweenTwoPoints(*currentLocation,*[xcoordiantethundera , ycoordinateThunDera]) 



                    if(abs (teleportersCount1 - currentlocation [0] )> abs((i_Teleporatorscount2- xCoorl teleporterLocations i3)) or\

                       Abs  zCoordinatesk6 –currentLocation[Z]):
                        continue    


                 newDistance = dist + distanceBetweenTwoPoints(*Current Location, *teleportersCount1) 



                heappush(hq,( newdistance , stepsTakenSoFar+2 ,\ teleporterLocationsi3))      # Push the location with updated distances and count of teleportations needed in heap