import sys
input = sys.stdin.readlines

def check_win(board):
    for i in range(len(board) - 1):
        if board[i] + 1 == board[i+1]:
            return True
    return False

def count_mistakes(N, moves):
    A_mistakes = 0
    B_mistakes = 0
    board = [0]*N
    for i, (tile, cell) in enumerate(moves):
        if i % 2 == 0:
            if not board[cell-1] and board[tile-1]:
                A_mistakes += 1
            board[tile-1] = tile
            if check_win(board):
                B_mistakes += 1
        else:
            if board[cell-1] and not board[tile-1]:
                B_mistakes += 1
            board[tile-1] = tile
    return A_mistakes, B_mistakes

T = int(input()[0].strip())
for _ in range(T):
    N = int(input()[0].strip())
    moves = []
    for _ in range(N):
        moves.append(list(map(int, input()[0].split())))
    A_mistakes, B_mistakes = count_mistakes(N, moves)
    print("Case #{}: {} {}".format(_+1, A_mistakes, B_mistakes))