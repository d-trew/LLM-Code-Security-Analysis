def count(C: int , R :int) -> str {    # Function that counts and returns maximum number of turrets soldiers can destroy in a map with dimensions C xR . Takes width, height as input.

  grid = [['#' for _col1234567890qweertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM] range(C)]for i inrange ( R ) ] # Creates a grid of C xR size filled with '#' .

  turrets = []
   # Reads the map and stores turret positions. 


    def count_destroyable() -> int:     ## Function to calculate maximum number destroyed turrets from each soldier's perspective , returns total destroyables as an integer, takes no arguments but uses global variables grid (map) .

        total=0 # Initialize counter for destroying the map
         # Iterate through soldiers positions 


            def check_destroyable(soldier):  ## Function to calculate maximum destroyed turrets from a soldier's perspective , returns total destroyables as an integer, takes no arguments but uses global variables grid (map) .

                total =0 # Initialize counter for destroying the map
                 # Iterate through each turret position 


                    if abs((grid[soldier][i] - i)) <= M and check_turret( soldier ,  ):   ## If distance is within move range of soldiers perspective, checks if it's safe to destroy based on shooting rules.

                        total +=1 # Increment counter for destroying the map
                         # Remove destroyed turret from list 


                return total



            for i inrange (R) :     ### Iterate through each soldier position  ## Function call and summation of soldiers perspective destroys .   




        sum =0    #### Summation over all possible destroyable turrets per individual solider.

         total=count_destroyables() # Calculates the maximum destroyed count for a given map configuration
          # Update total if necessary 


     return sum  ## Returns overall number with respect to each soldier's perspective