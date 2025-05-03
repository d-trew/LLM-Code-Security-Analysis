T = int(input())
for t in range(T):
    board = []
    for i in range(6):
        board.append([])
        for j in range(6):
            board[i].append(list(input()))

    # Find the red cells
    red_cells = set()
    for i in range(6):
        for j in range(6):
            if board[i][j] == 'R':
                red_cells.add((i, j))

    # Check if there is a valid solution
    found_solution = False
    for i in range(8):
        for j in range(8):
            if len(red_cells) == 0:
                break
            for k in range(i, i + 2):
                for l in range(j, j + 2):
                    if (k, l) in red_cells:
                        red_cells.remove((k, l))
            if len(red_cells) == 0:
                found_solution = True
                break
        if found_solution:
            break

    # Output the solution
    if found_solution:
        print("Case #" + str(t + 1) + ": POSSIBLE")
        for i in range(8):
            for j in range(8):
                if (i, j) in red_cells:
                    print(".", end="")
                else:
                    print(" ", end="")
            print()
            for j in range(8):
                if (i, j) in red_cells:
                    print(".", end="")
                else:
                    print(" ", end="")
            print()
        print()
    else:
        print("Case #" + str(t + 1) + ": IMPOSSIBLE")