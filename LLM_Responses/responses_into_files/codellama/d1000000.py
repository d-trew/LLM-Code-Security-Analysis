import sys

def solve(N, S):
    """
    Given a list of N dice with different number of sides S_i, return the maximum length straight that can be formed using some or all of the dice.
    """
    # Initialize a dictionary to store the maximum integer for each die
    max_integers = {}
    for i in range(N):
        max_integers[i+1] = S[i]
    
    # Sort the dictionary by value in descending order
    sorted_max_integers = sorted(max_integers.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize a list to store the indices of the dice that can be used to form a straight
    valid_dice = []
    
    # Iterate through the dictionary and check if the current die can be used to form a straight
    for i in range(len(sorted_max_integers)):
        if sorted_max_integers[i][1] >= 5:
            valid_dice.append(sorted_max_integers[i][0])
    
    # Return the length of the straight
    return len(valid_dice)

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        S = list(map(int, input().split()))
        print("Case #" + str(t+1) + ": " + str(solve(N, S)))