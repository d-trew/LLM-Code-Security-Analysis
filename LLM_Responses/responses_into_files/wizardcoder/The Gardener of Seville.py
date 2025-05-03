import itertools
def hedge_maze(lovers):
    # Create the maze with all walls
    maze = [['/'] * (2*R+2) for _ in range(2*C+2)]
    
    # Add the lover pairs to the maze
    for pair in lovers:
        row1, col1, row2, col2 = pair[0]-1, pair[1]-1, pair[2]-1, pair[3]-1
        if row1 == row2 and col1 == col2:
            return "IMPOSSIBLE"
        
        # Check if the cells are adjacent
        if abs(row1 - row2) + abs(col1 - col2) != 1:
            continue
        
        # Connect the lovers with a diagonal path
        if row1 < row2 and col1 > col2:
            maze[row1][col1] = '\\'
            maze[row2+1][col2+1] = '/'
        elif row1 > row2 and col1 < col2:
            maze[row1][col1] = '/'
            maze[row2+1][col2+1] = '\\'
        
    # Check if all lovers are connected
    for i in range(R):
        for j in range(C):
            if maze[i][j] == '/':
                if maze[i-1][j+1] != '\\' and (i,j) not in lovers:
                    return "IMPOSSIBLE"
            elif maze[i][j] == '\\':
                if maze[i+1][j-1] != '/' and (i,j) not in lovers:
                    return "IMPOSSIBLE"
    
    # Remove the outer wall
    for i in range(2):
        for j in range(C+2):
            maze.pop(0)
        maze = list(itertools.chain(*maze))
        
    return ''.join(maze)
    
# Read test cases
T = int(input())
for i in range(1, T+1):
    R, C = map(int, input().split())
    lovers = []
    for _ in range(R*C//2):
        pair = list(map(int, input().split()))
        lovers.append([pair[0], pair[1], pair[3], pair[4]])
    
    # Generate the maze
    result = hedge_maze(lovers)
    
    print("Case #{}:".format(i))
    if result == "IMPOSSIBLE":
        print(result)
    else:
        for row in range(R+2):
            print(''.join(result[row*(C+2):(row+1)*(C+2)]))