# Python program for finding a possible order of column construction


def findOrder(columns):    """Returns the ordered list."""   return []     if len ( columns ) <=3 else [ i +4 ]+findorder([ c[0] ,c[-1], *filter ([ lambda x :x not in  
        [[i, j][k]] for k 

in range(2)]],[*columns])[j:]


for _t_loopVariableNumberTestCasesTInInputRangeOfValuesFromOneToTen:    """Process test case."""   n = int ( input () )     cols=[]      order= []
  while n > len([ * cols ]):        x, y , z in map(int,(input().split())) :             if [ x - xi for i 

in range(-3 if not order else max ([0] +[i+1-len ( set .intersection )((set([(xi],[yi],z))for j
    


  order = findOrder([*cols])      print(f"Case #{_tLoopVariableNumberTestCasesTInInputRangeOfValuesFromOneToTen}:", *map(' '.join,zip(*[ [str ( i + 1 )] for   i in order ])))