def main():
    T = int(input()) # number of test cases
    for i in range(1, T+1):
        N = int(input()) # number of tiles and cells on the board
        mistakes_A = 0
        mistakes_B = 0
        
        moves = []
        for j in range(N):
            M, C = map(int, input().split())
            moves.append((M,C)) # collect all the moves
            
        for j in range(1, len(moves)-1):
            if (moves[j][0] == moves[j-1][0]+1 and abs(moves[j][1] - moves[j-1][1]) == 1) or \
               (moves[j][0] == moves[j+1][0]-1 and abs(moves[j][1] - moves[j+1][1]) == 1):
                mistakes_A += 1 # mistake for A if two adjacent tiles are placed next to each other in a wrong way
            elif (moves[j][0] == moves[j-1][0]+1 and abs(moves[j][1] - moves[j+1][1]) != 1) or \
                 (moves[j][0] == moves[j+1][0]-1 and abs(moves[j][1] - moves[j+1][1]) != 1):
                mistakes_B += 1 # mistake for B if two adjacent tiles are not placed next to each other
                
        print("Case #{}: {} {}".format(i, mistakes_A, mistakes_B))
        
if __name__ == "__main__":
    main()