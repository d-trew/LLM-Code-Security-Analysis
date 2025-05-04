from itertools import combinations   # Import necessary library for generating subsets of elements in an iterable object such as sets and lists



def minDuckInfiltration(N: int, M :int , S  ): # Function to find the minimum number ducks infiltrated

     statements = []                 ## Initialize a list where statements will be stored
    for _i_statementNumberin range (S)   # Loop through each statement in input 


        A,_j_,U__k__,V___l,D____m  = map(int ,input().split()) # Read the ith line of test case and store as integers into variables

         statements.append([ A -1] + [ B-2 for i_statementNumberin range (M)])+list(( U_, V__k__, D___l)))   # Append each statement to statements list


    for k in reversed(range(-N, N)):  ## Iterate over all possible numbers of ducks from 0 till max number
        H = set()                      

         if not isFeasibleHypothesis([i for i_statementNumberin range (S) if any((k == A-1 and D > C ) or k in B)]) : # Check feasibility using the function below. If hypothesis isn't feasible, continue to next iteration
             continue


        H = set(range(-N + 2 *  max([U for U , _V__K__,_D___l]in statements) - max[C ]for C in [c]) if k == A-1 and D > c else B)) # Generate hypothesis based on the number of ducks 'k'

        return len(H )                  # Return minimum size H


def isFeasibleHypothesis (statements):   ## Function to check feasibility using statements
    paths = {}                        



     for i_statementNumberin range  : 




         A,B ,U_,V__K__,D___l= mapint,(input().split())

        if A in paths and B not set(path[a] for a _ path.values()): # If duck is already there but the other person isn't at that location then hypothesis will be invalid
            return False


         paths [A ] = (U_,V__K__)  # Store their locations as dictionary keys with values being tuples of coordinates

    for i_statementNumberin range(S): 



        if not paths.get[statements] or statements in set((a,b) for a , b _ path .values()): # Check if the statement is valid based on hypothesis and stored location
            return False


     paths = {}  # Reset dictionary after checking each line of input

    for i_statementNumberin range(S): 



        A B U_,V__K__,D___l= mapint,(input().split())