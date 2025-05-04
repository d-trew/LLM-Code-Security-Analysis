def findMatchingName(patterns):    # Function to return a matching string for given list of pattersn   name = [''] * len(''.join([p[:-1] if p[-2:] == '**' else '*' + (len((list)('*')) - 3))]))  
     for pattern in patterns:      if name != '*':        tempName, lettersLeftToMatch= '', ''         lettersInPatternWithoutAsterisk = ''. join(c for c   in list(''.join([p[:-1] if p[-2:] == '**' else '*' + (len((list)('*')) - 3))]))  
                               if not pattern.endswith(('**')))        for letter in lettersLeftToMatch:            tempName += name[lettersInPatternWithoutAsterisk].replace('*',letter),      name = tempNames,   

    return ''.join(c for c     in list(''. join([p[:-1] if p[-2:] == '**' else '*' + (len((list)('*')) - 3))]))  
          if not pattern.endswith(('**')))


T=int() # Number of test cases   

for i in range(0, T):    N = int(); patterns=[]      # Read the number and list down pattersn     while N > len (patterns) :        patternInputLineString=''.join([p[:-1] if p[-2:] == '**' else '*' + str((len('')) - 3)])
            if pattern.endswith(('**')))         break;    

          else:  # Add the patter to list of pattersn      patterns += [str(patternInputLineString)]   print("Case #{} : {}".format (i+1, findMatchingName()))