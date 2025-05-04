def minExchanges (C: list[int], D :list [ int ], J  = [] , K = []) -> str {        # Calculate the total time of Cameron's activities in minutes     totalCameronTime   sum(D)      

 #Calculate Jamie and his activity times 


 def calculateJamieTimes():
    for i, (startJtimei_inMinutes,)K): enumerate() :  if startjtimieInminutes <= C[-1] < K[I]: return True ;return False;        # Calculate the total time of James' activities in minutes     totalJamesTime   sum(k)      

 # Check if Cameron and Jamie have enough activity times to cover for each other 


 def checkTotalTimes():
    if ( totalsCamerontime + sumJtimes ) >  720: return False;return True ;        # Calculate the minimum number of exchanges required using a greedy approach     exchanges = [totalJamesTime] - totalCameronTIme   

 # Print results for each test case 


 def printResults():
    for i in range(T):      print("Case #" + str (i+1)  ": " ,minExchages[I]) ;