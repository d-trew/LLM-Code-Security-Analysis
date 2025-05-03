def count_mistakes(N, moves):
    def can_win(board, player):
        for i in range(len(board) - 1):
            if abs(board[i] - board[i + 1]) == 1:
                return True
        return False

    def is_winning_state(board, player):
        temp_board = board[:]
        for i in range(N):
            if temp_board[i] == 0:
                for j in range(1, N + 1):
                    if j not in temp_board:
                        temp_board[i] = j
                        if player == 'A':
                            if can_win(temp_board, 'B'):
                                return True
                        else:
                            if can_win(temp_board, 'A'):
                                return False
                        temp_board[i] = 0
        return player == 'A'

    def is_mistake(board, move, player):
        board[move - 1] = moves.pop(0)
        if not is_winning_state(board[:], player):
            board[move - 1] = 0
            return False
        return True

    results = []
    for _ in range(N):
        N = int(input().strip())
        moves = [int(x) for x in input().strip().split()]
        board = [0] * N
        player_A_mistakes = 0
        player_B_mistakes = 0

        for i in range(N):
            if i % 2 == 0:
                move = moves.pop(0)
                if is_mistake(board[:], move, 'A'):
                    player_A_mistakes += 1
            else:
                move = moves.pop(0)
                if is_mistake(board[:], move, 'B'):
                    player_B_mistakes += 1

        results.append((player_A_mistakes, player_B_mistakes))

    for i, (a, b) in enumerate(results):
        print(f"Case #{i + 1}: {a} {b}")