# Sample case #1: Two players with different moves   print("Case {}:\n{}".format(test+2,"PR"))    return


def generateLineupForTestCases():      for test in range (T):        N, R , P = mapint(), input().split())       S= N-R -P  # Scissors player count     if S == 0:          print("Case {}:\n{}".format(test+2,"IMPOSSIBLE"))            continue    lineup_list =[]   for i in range (1,(N//3)+4):        rock = 'r' *i      paper= "p"*(R-len)
scissors ="s"(S - len )       if rock and paper or scissors:          print("Case {}:\n{}".format(test+2,"IMPOSSIBLE"))            continue    lineup_list.append(''.join([rock,Paper ,Scissors]))   return sorted ( lineups  for lineup in Lineup) [0]