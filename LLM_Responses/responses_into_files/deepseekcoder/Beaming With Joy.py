def solve():
    T = int(input())
    for t in range(T):
        R, C = map(int, input().split())
        grid = [list(input()) for _ in range(R)]
        beam_shooters = []
        empty_cells = 0
        
        # Find all beam shooters and count the number of empty cells
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '|' or grid[i][j] == '-':
                    beam_shooters.append((i, j))
                elif grid[i][j] == '.':
                    empty_cells += 1
        
        # If there are no empty cells, we can return POSSIBLE without rotating any beam shooter
        if not empty_cells:
            print(f'Case #{t+1}: POSSIBLE')
            continue
        
        # Check each possible rotation for the beam shooters
        for i in range(4):  # A total of 4 rotations (0, 90, 180, 270 degrees)
            if check_rotation(grid, R, C, beam_shooters, empty_cells):
                print(f'Case #{t+1}: POSSIBLE')
                return
            
            rotate_beam_shooters(R, C, beam_shooters)
        
        print(f'Case #{t+1}: IMPOSSIBLE')
    
def check_rotation(grid, R, C, beam_shooters, empty_cells):
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.':
                continue
            
            # Check each beam shooter and its beams
            for x, y in beam_shooters:
                dx, dy = x - i, y - j  # Direction of the beam from the beam shooter
                
                if (dx, dy) == (-1, 0):  # Beam is going up
                    k = 0
                    while 0 <= x + k < R and grid[x+k][y] != '#':
                        if grid[x+k][y] == '|' or grid[x+k][y] == '-':
                            empty_cells -= 1
                            break
                        k += 1
                elif (dx, dy) == (0, 1):  # Beam is going right
                    k = 0
                    while 0 <= y + k < C and grid[x][y+k] != '#':
                        if grid[x][y+k] == '-' or grid[x][y+k] == '|':
                            empty_cells -= 1
                            break
                        k += 1
                elif (dx, dy) == (1, 0):  # Beam is going down
                    k = 0
                    while 0 <= x + k < R and grid[x+k][y] != '#':
                        if grid[x+k][y] == '|' or grid[x+k][y] == '-':
                            empty_cells -= 1
                            break
                        k += 1
                elif (dx, dy) == (0, -1):  # Beam is going left
                    k = 0
                    while 0 <= y + k < C and grid[x][y+k] != '#':
                        if grid[x][y+k] == '-' or grid[x][y+k] == '|':
                            empty_cells -= 1
                            break
                        k += 1
            
            if not empty_cells:
                return True
    
    return False

def rotate_beam_shooters(R, C, beam_shooters):
    for i in range(len(beam_shooters)):
        x, y = beam_shooters[i]
        
        if (x, y) == (-1, 0):  # Beam shooter is going up
            beam_shooters[i] = (y - R + 1, C - x - 1)
        elif (x, y) == (0, 1):  # Beam shooter is going right
            beam_shooters[i] = (-(C - y - 1), x + R)
        elif (x, y) == (1, 0):  # Beam shooter is going down
            beam_shooters[i] = (y + R + 1, C - x - 1)
        else:  # Beam shooter is going left
            beam_shooters[i] = (-(C - y - 1), x - R)

solve()