from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    cards = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Sort the deck by rank and suit
    cards.sort()
    
    # Initialize a deque to hold the operations
    ops = deque()
    
    # Perform the operation as long as there are more than 1 card left
    while len(cards) > 1:
        # Find the maximum rank and suit in the remaining cards
        max_rank, max_suit = 0, 0
        for r, s in cards:
            if (r > max_rank) or (r == max_rank and s > max_suit):
                max_rank, max_suit = r, s
        
        # Find the position of the maximum card in the deck
        pos = 0
        for i, (r, s) in enumerate(cards):
            if (r == max_rank and s == max_suit):
                pos = i
                break
                
        # Perform the operation: take all cards from the top of the deck to form pile A
        pileA = [cards.pop() for _ in range(pos+1)]
        
        if len(cards) > 0:
            # Take one card from the new top of the deck to form pile B
            pileB = [cards.pop()]
            
            ops.append((pileA, pileB))
    
    print(len(ops))
    for a, b in ops:
        print(len(a), len(b))
        
T = int(input())
for tc in range(1, T+1):
    print("Case #{}: ".format(tc), end="")
    solve()