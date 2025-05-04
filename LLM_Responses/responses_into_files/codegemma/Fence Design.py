from itertools import combinations as combnns  # Import necessary library for generating all pairs between two sets



def maxFencing(N, poles):    # Function to calculate maximum number of fences and their locations given the pole positions.


    existing = set()        ## Initialize an empty list/set
                             ###to store existing fence connections

                            for i in range (1,(len((poles)))+ 2)):  # Iterate over all pairs between poles, excluding collinear ones using if condition below:   if len(list({pole[0], pole [3]} for pair_of Poles) == set()) >
        existing.add(((i),(j)))


    maxNum = N - (len((poles)))+ 2 + sum([1  for i in range ((N-4):)]) # Calculate maximum number of fences allowed based on the total possible pairs between poles and existing ones

   pairs_ofPoles= list(combnns(*zip(*(pole for pole, _ ,__in enumerate (list((poles)))))) ) 
    # Generate all unique combinations without duplicates using itertools.combinations


  fences = set() # Initialize an empty dictionary to store new fence connections in a specific format

   for i,(p1),(q2) pair_ofPoles:     ## Iterate over each possible combination of two poles as endpoints for the newly added fences
        if (pair(min((i,j)), max ((a.b))) not existing): # Check if new fence connects already built ones or forms a collinear line with three points

            fences += [p1 q2]  # Add pair to set of valid connections


    return len(' '.join([str (x) str(y)]) for x, y in fences), '\n'. join(['{} {}'.format(*pair)]for pairs_ofPoles)) # Return the maximum number and a formatted list with endpoints.



if __name__ == "__main__":  # Main program
    T = int((input()))   ## Read input from user about total test cases


     while T > 0:

        N=int(sys().stdin) ## Number of poles in each case is read here as N




         poles=[] # Initialize an empty list to store pole positions.



          for i  in range (1,(len((pole)))+2):
            x,y = map(((lambda x : int)(input()))), str(sys().stdin).split())

             ## Read and append the coordinates of each poles in a pair 


         existing=[] # Initialize an empty list to store existing fences.



          for i  in range (1,(len((pole)))+2):
            x,y = map(((lambda x : int)(input()))), str(sys().stdin).split())

             ## Read and append the coordinates of each pair representing endpoints for already built fence in a set


        max_fences , fences= maxFencing (N + poles)  # Call function to calculate maximum number, formatted list with new connections.



         print('Case #{}: {}'.format(T,(MaxNum)))

          for i and j range((len((' '.join([str x] str y)]) for X in fence))):
              sys().stdout = open("output", "a")  # Open file to write the output of each case


             print(' {}' . format (i,j),file= sys.stdin)

          T -= 1 # Decrement test cases counter