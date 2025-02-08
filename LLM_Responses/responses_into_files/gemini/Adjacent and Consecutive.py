def solve():
    N = int(input())
    moves = []
    for _ in range(N):
        moves.append(list(map(int, input().split())))

    board = [0] * N
    tiles_used = set()
    
    a_mistakes = 0
    b_mistakes = 0

    def is_winning(current_board, available_tiles):
        for i in range(N - 1):
            if (current_board[i] != 0 and current_board[i+1] != 0 and 
                abs(current_board[i] - current_board[i+1]) == 1):
                return True
        return False

    def check_mistake(player, current_board, available_tiles, move):
        
        if is_winning(current_board, available_tiles):
          
            new_board = current_board[:]
            new_board[move[1]-1] = move[0]
            new_available_tiles = available_tiles - {move[0]}
            
            can_opponent_win = False
            
            for tile in new_available_tiles:
                for i in range(N):
                    if new_board[i] == 0:
                        temp_board = new_board[:]
                        temp_board[i] = tile
                        if is_winning(temp_board, new_available_tiles - {tile}):
                            can_opponent_win = True
                            break
                if can_opponent_win:
                    break
            return can_opponent_win

        return False
            

    for i in range(N):
        move = moves[i]
        board[move[1]-1] = move[0]
        tiles_used.add(move[0])
        available_tiles = set(range(1,N+1)) - tiles_used
        
        if i % 2 == 0: #Player A's turn
            if check_mistake("A", board[:], available_tiles, move):
                a_mistakes +=1
        else: #Player B's turn
            if check_mistake("B", board[:], available_tiles, move):
                b_mistakes += 1

    return str(a_mistakes) + " " + str(b_mistakes)

T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")