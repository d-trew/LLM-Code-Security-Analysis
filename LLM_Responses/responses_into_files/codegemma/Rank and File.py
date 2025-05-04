# -*- coding : utf-8 -*   


def findMissingList(heightLists):    """ Finds and returns a complete row or column heightlist based on two partially known lists """     



	rowHeightSet = set()        

for heights in [heights for i, 		      			
					       				  							            						          								                            									           										   in enumerate (history) if not(i %2)]:    # Iterate over odd numbered lines to get row heightset                                                


     if len([h1- h3>0 and heights.count==	                          heightLists[int((len 		      			
					       				  							            						          								                            									           										   )/4)][i] for i,    # Check if there's a difference between row heightset & column list of same index in history                                                


     rowHeightSet.add(h)

	columnHeights = [heightLists[int((len 		      			
					       				  							            						          								                            									           										   )/4)][i] for i,    # Get the heights from first column list of every fourth line in history                                                


     missingList=[]        for h1-h3>0 and heightLists.count(height) > 	                          columnHeights[int((len (history))/2)]:  
         if not missingHeight:      		              			   						       								    							            					                       				             									           										          

                 break;     missingList=[x for x in rowHeighset if height!=h]        return [height]+sorted(columnHeights)


for t 	in range (int((input())))):  
      history = []                             # Initialize list to store heights from history                                               		    					   								                          							          									           										     

 for i in xrange ((2*n)-1)):       			        				              						         												                            											                       


            height= int(sys.stdin().readline())	  
             history += [int()]                 # Store the height of each row and column as we read them from history                                               		    					   								                          							          									           										     

 print("Case #{}: {}".format((t+1), findMissingList))