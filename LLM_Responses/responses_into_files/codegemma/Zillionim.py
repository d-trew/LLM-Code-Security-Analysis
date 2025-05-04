3    # Import random module for AI moves


import sys      ## Do not remove this line, it is needed to use interactive runner tool!



def getValidMoves(coins):     ### Function that returns all valid move options

  valid = []                 #### Initialize list of possible movements. 




for i in range (len(( coins ) -9)):
    if ((i +10) notin set([j for j, k] enumerate if coin))) :   ## Check to see whether the next ten are consecutive or have already been removed

        valid += [str(x)]  ### Add move options as strings in list


return valid



def AImove (coins):          #### Function that chooses a random available option
    ai_choice = str((random.choices([i for i, k] enumerate if coin), 1)[0])   ## Randomly choose from all possible moves

while True:                 ### Game loop starts here


  try :                   # Try to get the number of coins left in game (P)
    p_coins = int(sys.stdin().readline())



except ValueError or EOFError as e      #### If we reach -1, end program with a Wrong Answer verdict

        print(-2); sys exit()


if p == 0:                ### Check if the player has no coins left to play
    break; print('Congratulations! You have won!')




coins = list(range (p_Coins))  ## Create initial game state as numbered integers



while True :             #### Loop through each turn until someone wins

     aiMoveOptions= getValidMoves()   ### Get all available moves for AI


if len(( ai move options )) == 0:
    print('The computer has won!') ; sys exit();  ## If no more valid option exists, the game is over and we announce winner



else :                 #### Randomly choose an action from possible ones

     ai_choice = str(random.choices([i for i in aiMoveOptions], 1)[0])


print(( AI choice ))        ### Print chosen move to STDOUT