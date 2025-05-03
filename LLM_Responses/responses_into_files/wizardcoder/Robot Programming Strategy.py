import random
def play_move(robot1, robot2):
    if robot1 == "R" and robot2 == "P": return 0
    elif robot1 == "R" and robot2 == "S": return 1
    elif robot1 == "S" and robot2 == "P": return 1
    elif robot1 == "S" and robot2 == "R": return 0
    else: return -1 # tie
    
def play_match(robot1, robot2):
    while True:
        move1 = robot1.pop(0) if len(robot1) > 0 else robot1.extend(robot1[::-1]) or robot1.append("R") # reset and start over, or play the first move of the program
        move2 = robot2.pop(0) if len(robot2) > 0 else robot2.extend(robot2[::-1]) or robot2.append("R")
        
        result = play_move(move1, move2)
        if result == -1: # tie
            continue
        elif result == 0:
            return "L" # robot1 wins
        else:
            return "W" # robot2 wins
    
def play_tournament(robots):
    n = len(robots)
    while n > 1:
        for i in range(n//2):
            winner = play_match(robots[i], robots[n-i-1]) # the last bot is the loser of the first match, so it plays second
            if winner == "W":
                del robots[n-i-1] # remove the loser
        n //= 2
    return robots[0][::-1] # reverse the program to start at the beginning and end with the winning move
    
def main():
    T = int(input())
    for t in range(T):
        A = int(input())
        opponents = []
        for i in range(A):
            C = input()
            if len(C) > 50: # handle invalid input
                print("Case #{}: IMPOSSIBLE".format(t+1))
            else:
                opponents.append(list(C))
        robots = [play_tournament([opponent[i] for opponent in opponents if i % 2 == j] for j in range(A%2, A)) for _ in range(2)] # play each round separately
        print("Case #{}: {}".format(t+1, "".join(robots[-1]))
        
if __name__ == "__main__":
    main()