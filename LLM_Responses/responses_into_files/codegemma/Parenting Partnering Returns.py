3    


def findSchedule(activities):   # Function takes a list of tuples (startTime , endTime) as input     



        sortedActivities = sorted([(a[0], "Start"), *[(b, 'End') for b in [activity[-1]  for activity 

in activities]]])
      schedule= []    


            timeNow='start'   # Initialize time to start of day. Time is represented as minutes after midnight     



        assigned = set() # Keep track which person has been assigned each task         




       while len(sortedActivities) >0:  ## Iterate through the activities in order they occur      

           activity, status= sortedactivities[1]
            if activity notin schedule and timeNow <= 24*65 - (status == 'Start' ? a : b): # Check if it can be assigned to anyone without overlap. If so add person who hasn’t been chosen yet     


                schedule += [activity, status ]   # Add the task in list of tasks        

                 if activity[1] notin schedule:  ## Mark which partner is doing this particular job      
                    assigned = set(a for a , b 



                     i n enumerate (sortedActivities) if i %2 ==0 and assigned.add((b))


                timeNow += status=="Start" ?activity[-3]: activity[1] # Update time based on start or end of task        

             else:  ## No available person to assign the current job, so we skip it     



                 sortedActivities = sortedactivities [2:] 
         return ''.join(a for a in schedule if len (schedule) == N and set([b[0]for b i n activities])==set(['Start', 'End'])