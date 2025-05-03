from itertools import product

def rotate(tile):
    return [list(x[::-1]) for x in zip(*tile)]

def reflect(tile):
    return [x[::-1] for x in tile]

def is_valid_placement(board, tile, r, c):
    for i in range(3):
        for j in range(3):
            if board[r+i][c+j] != '.' and (board[r+i][c+j] == '!' or board[r+i][c+j] == '@'):
                return False
    return True

def place_tile(board, tile, r, c, char):
    for i in range(3):
        for j in range(3):
            if tile[i][j] != '.':
                board[r+i][c+j] = char

def remove_tile(board, tile, r, c):
    for i in range(3):
        for j in range(3):
            if tile[i][j] != '.' and (board[r+i][c+j] == '!' or board[r+i][c+j] == '@'):
                board[r+i][c+j] = '.'

def is_solution(board, tile1, tile2):
    for r in range(6):
        for c in range(6):
            if is_valid_placement(board, tile1, r, c):
                place_tile(board, tile1, r, c, 'A')
                if is_solution(board, tile2, tile1):
                    return True
                remove_tile(board, tile1, r, c)
    return False

def solve_puzzle(tile1, tile2):
    for red_cells in product(range(8), repeat=8):
        board = [['.' for _ in range(8)] for _ in range(8)]
        valid = True
        for i in range(8):
            if red_cells[i] == 0:
                continue
            r, c = divmod(i, 8)
            tile = [list(x) for x in tile1]
            if not is_valid_placement(board, tile, r, c):
                valid = False
                break
            place_tile(board, tile, r, c, chr(ord('!') + i))
        if not valid:
            continue
        if is_solution(board, tile2, tile1):
            return True
    return False

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        tile1 = [data[index:index+3] for index in range(index, index+9)]
        index += 9
        tile2 = [data[index:index+3] for index in range(index, index+9)]
        index += 9
        
        if solve_puzzle(tile1, tile2):
            results.append("POSSIBLE")
        else:
            results.append("IMPOSSIBLE")
    
    for i, result in enumerate(results, start=1):
        print(f"Case #{i}: {result}")

if __name__ == "__main__":
    main()