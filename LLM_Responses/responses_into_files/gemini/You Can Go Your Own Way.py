def solve():
    N = int(input())
    P = input()
    
    lydia_path = []
    curr_row, curr_col = 0, 0
    for move in P:
        if move == 'E':
            lydia_path.append((curr_row, curr_col, curr_row, curr_col + 1))
            curr_col += 1
        else:
            lydia_path.append((curr_row, curr_col, curr_row + 1, curr_col))
            curr_row += 1

    my_path = ""
    curr_row, curr_col = 0, 0
    
    for _ in range(N - 1):
        if (curr_row, curr_col, curr_row, curr_col + 1) not in lydia_path:
            my_path += "E"
            curr_col += 1
        else:
            my_path += "S"
            curr_row += 1
            
    for _ in range(N - 1):
        if (curr_row, curr_col, curr_row + 1, curr_col) not in lydia_path:
            my_path += "S"
            curr_row += 1
        else:
            my_path += "E"
            curr_col += 1

    return my_path


T = int(input())
for i in range(1, T + 1):
    result = solve()
    print(f"Case #{i}: {result}")