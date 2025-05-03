import sys

def solve(R, C):
    board = [['.' for _ in range(C)] for _ in range(R)]
    for i in range(R):
        line = list(input())
        for j in range(C):
            if line[j] == '#':
                board[i][j] = '#'
    winning_moves = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'H'
                winning_moves += check_winning_moves(board, R, C)
                board[i][j] = '.'
                board[i][j] = 'V'
                winning_moves += check_winning_moves(board, R, C)
                board[i][j] = '.'
    print(f"Case #{R*C}: {winning_moves}")

def check_winning_moves(board, R, C):
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                return 1
    return 0

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    solve(R, C)