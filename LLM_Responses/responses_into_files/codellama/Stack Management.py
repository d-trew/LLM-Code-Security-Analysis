import sys
input = sys.stdin.readline

def solve(N, C):
    # Initialize a dictionary to store the cards in each stack
    cards = {}
    for i in range(N):
        cards[i] = []
    
    # Add the premade stacks to the dictionary
    for i in range(len(C)):
        cards[i] = C[i]
    
    # Check if it is possible to win the game
    for i in range(N):
        for j in range(len(cards[i])):
            value, suit = cards[i][j]
            if value + 1 == cards[i][j+1][0] and suit == cards[i][j+1][1]:
                # If there is a sequence of cards with the same value/suit combination, return True
                return True
    # If no sequence of cards with the same value/suit combination is found, return False
    return False
    
# Read the input
N = int(input())
C = []
for i in range(N):
    C.append([int(x) for x in input().split()])

# Check if it is possible to win the game
if solve(N, C):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")