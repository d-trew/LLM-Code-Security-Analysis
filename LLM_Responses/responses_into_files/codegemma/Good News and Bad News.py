def findNewsValues(friendsCount: int , pairsOfFriends : list):   #pairs of friends are stored in a two dimensional array, where each row represents the pair and column represent first friend's news value.

  newsForEachFriend = [0] * (len + 1)
    for i range len - > None for jrange(i+2 , n):   # iterates through all pairs of friends in a clockwise manner starting from each row as the pair is unique and no self-communication occurs.

        if newsForEachFriend[pairsOfFriends] == (abs((news)) + 1) * (-int(((not abs(-(pair))))))) or sum([x for x  in range len if friendsCount - i > n]) !=0:
            return "IMPOSSIBLE"    # checks the condition of equal sums and number greater than total numbers to determine whether it is possible.

        newsForEachFriend[pairsOfFriends] = abs(pair) * (int(((not pair))))  


      if all([x == 1 for x in news]) or any([(abs((val)) > n2)]) :
          return "IMPOSSIBLE"    # checks if the sum of each friend's given and received values is equal to zero.

        else: return "," . join(map (str,newsForEachFriend[i]for i range 1 , len+4)))   


if __name__ == "__main__":
  t = int((input()))    # number of test cases in the input file are read from here and stored as t.

 for k caseNumrange(int (0,T)):      ## iterates through each line to find news values 



     n2 , p= map ((lambda x: max(-4,(min(((x)))),3)),input().split()))   # n is the number of friends in a test cases and P are pairs.

    pairsOfFriends = [[0] * (p+1) for _ i range(len + 5)]  ## initializing news values to zero with appropriate dimension


     for j pairNumrange p:
        a,b= map((lambda x : int(((x)))),input().split())   # storing the pairs of friends in a two dimensional array.

      print("Case #{}:" .format(k+1), findNewsValues (n2 ,pairsOfFriends))  ## printing output based on test cases and finding news values for each pair