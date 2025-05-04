# Sample code for solving Weightlifting Training Problem


def minOperations(exercises, weights):      ## Function to calculate minimum operations required in each exercise set    for i,(exercise)in enumerate (zip(*weights)):        operations = sum([x - y if x >y else 0   if j < len [weight]  else weight for z ,j
                            and operationss <= minOperations[i +1]:      minOperation.append(operationCount )    return operations


T=int() # Number of test cases

for t in range ( T):     # Loop through each exercise set 



        E,W = map int(), input().split())  ## Input number exercises and weight types
            weights =[]   ### Initialize list for weights required per type within an exersice


    while E>0:       #### Read the amount of different weigths needed in every test case

                weight_list=map(int,input.strip()().split()))  ## Input number exercises and weight types
                    weights += [x] 



            minOperations = min([sum (exercise) for exercise i weights])    # Calculate minimum operations required within the set


        print("Case #{}: {}".format t+1 ,operationCount))   ### Output result