import sys

def cleanup(balls, power):
    # Initialize variables
    current_power = 0
    target_power = power
    moves = []
    
    # Iterate through the balls and calculate the minimum number of moves needed to collect them all
    for ball in balls:
        if ball != 0:
            # If the current ball is not a 0, add a move to the list
            moves.append(ball)
        elif len(moves) > 0:
            # If the current ball is a 0 and there are previous moves in the list, deposit the previous balls
            for i in range(len(moves)):
                if moves[i] == 1:
                    target_power += power
                else:
                    target_power -= power
            current_power = target_power
            moves = []
    
    # If there are any remaining balls, add a move to the list to deposit them
    if len(moves) > 0:
        for i in range(len(moves)):
            if moves[i] == 1:
                target_power += power
            else:
                target_power -= power
        current_power = target_power
    
    # Return the minimum number of units of power needed to collect all the balls
    return current_power

# Read input from stdin
balls = list(map(int, input().split()))
power = int(input())

# Print the minimum number of units of power needed to collect all the balls
print("Case #1:", cleanup(balls, power))