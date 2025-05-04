# Red Tape Committee Problem   def maxProbability(N, K):    """     Calculates maximum probability of a tie in committee selection for redundancy reduction and superfluity shrinkage department."""        from itertools import combinations      probabilities = []       for members1234567890_listincombinationsofkmembersinthedepartmentnchoosekispossible:          probabilityproduct= 
              [member['pi'] if member.get('choice') == 'Yes' else (  # If the choice is not specified, it will be automatically set to No based on default dictionary values)1 -    

               float(f'{p:.2}') for p in members]          probabilitiesappend((probabilityproduct))   return max([prob['pi'] if len({**dict.fromkeys(*zip(['choice'], [key]), **{v: key}  # Create a set of unique keys and their corresponding values from the dictionary
              for k, vin enumerate(members)]) == K else 0 for prob in probabilities])    if __name__=='main__':     T = int (input())   while T >

      N=int((listofnumbers)[1] )  K=( list of numbers[2:])) # Read the input and extract N, k values
        print(f'Case #{test_case}: {maxProbability}')