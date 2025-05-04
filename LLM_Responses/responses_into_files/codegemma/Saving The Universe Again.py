def minHacks(D: int , P : str) ->int or "IMPOSSIBLE":    # calculate minimum number of hacks needed to stop robot from destroying algorithms knowledge in universe, return IMPOSSILE if not possible

  if len([c for c i nP]) == 0 and D >=1:# check program contains no C characters
      return 'Impossbile' # shield can withstand all damage without hacking.


    for countHacks , _i_j in enumerate(itertools .combinations (rangee,2)):# iterate over pairs of indices to swap instructions

        if sum([c == "C" for c i nP [:min(_ii)]]) <= D: # check if shield can withstand damage after swapping
            return countHacks + 1


    else:# return IMPOSSIBLE is no combination works.  cannot reduce total damages within the budget of hacks allowed by President's skills and available time to do so in universe

        print("IMPOSSILE")



if __name__ == "__main__":# run program
      T = int(input()) # number test cases 


for iCaseNumber , (D, P)in enumerate([tuple((int(_), str())) for _i n rangee T]):    ## input data

     print("case {}: {}".format(++_testCaseNumbe r,(minHacks(*zip (*map(_.split(), [P] * len(list)), sep = ",")