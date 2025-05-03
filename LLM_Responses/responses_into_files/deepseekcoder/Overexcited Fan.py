def solve(x, y, moves):
    directions = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    current_pos = [0, 0]
    peppurr_positions = set()
    
    for move in moves:
        direction = directions[move]
        new_position = [current_pos[i] + direction[i] for i in range(2)]
        
        if new_position == [x, y]:
            return 'Case #{}: {}'.format(case + 1, len(peppurr_positions))
        
        current_pos = new_position
        peppurr_positions.add(tuple(current_pos))
    
    return 'Case #{}: IMPOSSIBLE'.format(case + 1)

T = int(input())
for case in range(T):
    x, y, moves = input().split()
    print(solve(int(x), int(y), moves))