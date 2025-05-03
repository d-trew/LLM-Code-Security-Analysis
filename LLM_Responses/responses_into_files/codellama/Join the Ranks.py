import sys

def solve(R, S):
    """
    Given the number of ranks R and suits S in a deck of cards, find a sequence of operations that reorders the
    deck to be sorted by rank, as described above, and uses the minimum possible number of operations to do so.
    """
    # Initialize variables for the current piles and the number of operations needed
    A = []
    B = []
    ops = 0

    # While there are still cards in the deck
    while len(A) + len(B) < R * S:
        # If there are enough cards in the top pile to form a new pile of size A, do so and increment the number of operations
        if len(A) + 1 <= R - len(B):
            ops += 1
            B.append(A.pop())
        # Otherwise, take one card from the bottom of the deck and add it to the top pile, also incrementing the number of operations
        else:
            A.insert(0, B.pop())
            ops += 1

    # Return the minimum number of operations needed to reorder the deck
    return ops

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        R, S = map(int, input().split())
        print("Case #" + str(t+1) + ": " + str(solve(R, S)))