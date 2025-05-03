def main():
    T = int(input())
    for i in range(1, T+1):
        board_left = []
        board_right = []
        for j in range(3):
            board_left.append(list(input().split()[0]) + list(input().split()[1]) + list(input().split()[2]))
            input()
            board_right.append(list(input().split())
        print("Case #{}: {}".format(i, solve(board_left, board_right)))

def solve(board_left, board_right):
    for tile in itertools.permutations(['A', 'B']):
        if is_valid_solution(board_left, board_right, tile[0], tile[1]):
            print_grid(board_left, board_right, tile)
            break
    else:
        return "IMPOSSIBLE"
    return "POSSIBLE"

def is_valid_solution(board_left, board_right, tile1, tile2):
    for i in range(3):
        for j in range(3):
            if not (tile1[i*3+j] == '.' and tile2[i*3+j] == '.' or tile1[i*3+j] != '.') ^ (tile2[i*3+j] != '.'):
                return False
    for i in range(3):
        for j in range(3):
            if board_left[i][j] == '@' and tile1[i*3+j] == '.':
                return False
    for i in range(8):
        for j in range(8):
            if board_right[i//2][j//2] == '.' and (tile2[(i%2)*3+(j%2)] != '.' or tile1[(i%2)*3+(j%2)] != '.') ^ (tile2[(i%2)*3+(j%2)]) == '.':
                return False
    for i in range(8):
        for j in range(8):
            if board_right[i//2][j//2] == '@' and tile1[(i%2)*3+(j%2)] != '.' and tile2[(i%2)*3+(j%2)].isalpha():
                return False
    for i in range(8):
        for j in range(8, 16):
            if board_left[i//2][j//2] == '@' and tile2[(i%2)*3+(j%2).isalpha()]:
                return False
    return True

def print_grid(board_left, board_right, tiles):
    for i in range(8):
        print("".join([tiles[0] if (i//2)*3 + j//2 < 3 else '.' for j in range(17)]), end=' ')
        print("".join([board_left[(i%2)*3+j//2][(i//2)*3+j%2] if board_left[(i%2)*3+j//2][(i//2)*3+j%2] == '@' else tiles[1] for j in range(8)]), end=' ')
        print()
    print(" " * 9, end='')
    for i in range(8):
        print("".join([tiles[1] if (i//2)*3 + j//2 < 3 else '.' for j in range(17)]), end=' ')
        print("".join([board_right[(i%2)*3+j//2][(i//2)*3+j%2] if board_left[(i%2)*3+j//2][(i//2)*3+j%2] == '@' else tiles[0] for j in range(8)]), end=' ')
        print()
    return True

if __name__ == "__main__":
    main()