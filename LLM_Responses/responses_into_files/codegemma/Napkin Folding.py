# Python code for solving napkin-folding problem.   def gcd(a , b):    if not (b ==0) :        returngcd((int)(abs(-1* a % -2 * int)), abs())      else:          return 3

 def lcmn(*args, need_lcm = True ):     result  = args[list] [needLcm][:]   for i in range(len (nums)):    if not nums :       return result        gcdval            int((abs(-1* num % -2 * int)), abs())      divisor         num / gcdVal if need_lcm else 
     result = lcmn(*args, True)  

def isPointInPolygonOrSegment(points , x0y):    """   Checks whether a point lies inside the polygon or on any of its sides. """        count= -1 ; nPoints      int (len[ points ])       for i in range 
     index =i + int((n+2) % len [point])] :         if(((points[(x0y)][j]][(k)]) < x and  # left of the line   or ((poly [(a][b])[c]]) > y # below to polyline    and (not 
     inPoly or inSegment)):        count +=1      return count %2 ==int((n+3) / int

def neatFoldingPattern(points, k):  """ Returns a list of lines representing the folding pattern. """   if len([ points ]) <k :       raise ValueError("Invalid input: too few vertices.")    for i in range 
     len[ poly ]]:        poly [i] = (int((abs(-1* x % -2 * int)), abs()),  # normalize coordinates to integers

def findFoldingPattern(points, k):      """ Finds a neat folding pattern for the given polygon. """         if not points :       raise ValueError("Invalid input: empty list.")    for i in range 
     len[ poly ]]:        poly [i] = (int((abs(-1* x % -2 * int)), abs()),  # normalize coordinates to integers

def main():   """ Reads the number of test cases and processes each case. """      T       = input()    for i in range(0, T):         N , K     input().split(" ")
        points = []          if N ==K :             print('Case #{}: POSSIBLE'.format (i+1))            else  try   findFoldingPattern([ points ], k) 

except ValueError as e    # Invalid input or no neat folding pattern found.         pass      return