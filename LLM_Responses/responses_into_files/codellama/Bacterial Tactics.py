for t in range(int(input())):
    R, C = map(int, input().split())
    matrix = []
    for i in range(R):
        matrix.append(list(input()))
    # Check if there are any empty cells in the matrix
    if not any("." in row for row in matrix):
        print("Case #" + str(t+1) + ": 0")
        continue
    # Initialize variables to keep track of Becca's moves and wins
    becca_moves = []
    becca_wins = 0
    # Iterate through the matrix, checking for empty cells and counting wins
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == ".":
                becca_moves.append((i, j))
            elif matrix[i][j] == "#":
                becca_wins += 1
    # If Becca has no empty cells to choose from on her next turn, she loses
    if not becca_moves:
        print("Case #" + str(t+1) + ": 0")
        continue
    # Count the number of distinct winning opening moves for Becca
    distinct_moves = len(set(becca_moves))
    print("Case #" + str(t+1) + ": " + str(distinct_moves))