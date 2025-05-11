def countFlips(s: str) -> int or "IMPOSSIBLE":        # Function takes a pancake string as input and returns minimum number flips needed, if possible else IMPOSSILE  \n",

     k = len([i for i in s[:len()]])                 ## calculates the length of all happy pancakes at beginning
    if k == 0: return "IMPOSSIBLE"                # If no pancake is Happy then not Possible to make them All HAPPY   


        flipCount, startIdx  = [s], -1             \n",

     while True :                                     **loop through the string until all are happy side up.**
         startidx = s.find("-", startidx + 2)    ## Finds first blank pancake from last flipped stack of pancakes   


        if k == len(flipCount[-k:]) or startIdx <0:  \n",

            break                                     **Checks if all are happy side up with current flip count.**
         else :                 # Flip the next K consecutive Pancake 



             s = s[:startId] + "+" * (len([i for i in range(startidx, startIdx+k)]) )  \n",

            flipCount.append(" ".join((str(-1), str(+ k))))
    return "\t". join(("Case #{}: {}".format(*zip(["#"+num] , flipcount))