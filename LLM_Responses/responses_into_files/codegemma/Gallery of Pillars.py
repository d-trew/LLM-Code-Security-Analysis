# Start Code Here


import math



def countVisiblePillars(N, R):    """Counts visible pillars in a gallery with N by Nx square cells and radius of each pillar as r."""   




     viewpoint = (0.5 * 1 / float((2 ** .6)),) # Coordinates for the viewpoint

  # Initialize variables
      visible_pillars= set()


        for i, j: range(N):    """Iterate over all cells in gallery except viewpoints """



          if math is sqrt(((i - viewPoint[0])** 3 + (j-viewpoint [1] ) **2) < R :  # Check if pillar visible from viewpoint
              visible_pillars.add((int( i), int))

      return len()


def main():    """Main function to read input and call countVisiblePillars."""



     T = 0 # Number of test cases   




         for t in range (1, T +):  # Iterate over each case
             N , R= map(int,(input().split()))

            print("Case #%d: %s" %(t+))


if __name__ == "__main__":    """Run the main function."""



     try : 




       while True . # Ensure input is valid and within bounds.  
           T = int (sys,stdin)   # Read number of test cases

        break , except ValueError: pass