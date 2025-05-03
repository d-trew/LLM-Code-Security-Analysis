def calculate_mistakes(n, moves):
    # Initialize counters for each player
    mistakes = [0, 0]
    
    # Iterate over the moves
    for i in range(1, n+1):
        if i % 2 == 0:
            player = 1
        else:
            player = 0
        
        # Check if current move creates a winning state
        if abs(moves[i-2][0] - moves[i-1][0]) == 1 and (moves[i-2][1] == moves[i-1][1] or moves[i-2][1]+1 == moves[i-1][1] or moves[i-2][1]-1 == moves[i-1][1]):
            # If current move creates a winning state, the other player made a mistake
            mistakes[player] += 1
    
    return mistakes

# Read number of test cases
t = int(input())
for case in range(1, t+1):
    n = int(input())
    moves = []
    
    # Read the moves
    for _ in range(n):
        m, c = map(int, input().split())
        moves.append((m, c))
        
    mistakes = calculate_mistakes(n, sorted(moves))
    
    print("Case #{}: {} {}".format(case, mistakes[0], mistakes[1]))